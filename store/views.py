from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import get_object_or_404
from .models import Store, Review
from .forms import ReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied

# Create your views here.
'''
    store_list
    store_detail
    create_store
    update_store
    create_review
'''
class StoreList(ListView) :
    model = Store
    ordering = '-pk'
    template_name = 'store/store_list.html'

    def get_context_data(self, **kwargs) :
        context = super(StoreList, self).get_context_data()
        return context

class StoreDetail(DetailView) :
    model = Store

    def get_context_data(self, **kwargs) :
        # Comment form
        context = super(StoreDetail, self).get_context_data()
        context['comment_form'] = ReviewForm

        # Review
        reviews = Review.objects.filter(post=self.kwargs['pk'])
        sum_rate = 0
        cnt = 0
        for review in reviews :
            sum_rate += float(review.rating)
            cnt = cnt + 1
        aver_rating = sum_rate / cnt
        context['average_rating'] = aver_rating

        # Check seat
        # Get seats
        seats = Store.objects.filter(pk=self.kwargs['pk'])
        table = 0
        for seat in seats :
            table = seat.table
        table_list = [[i, False] for i in range(table)]
        context['table_list'] = table_list

        return context

class StoreCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView) :
    model = Store
    fields = ['title', 'address', 'content', 'table', 'head_image']

    def test_func(self) :
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form) :
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser) :
            form.instance.author = current_user
            response = super(StoreCreate, self).form_valid(form)
            return response
        else :
            return redirect('/store/')

class StoreUpdate(LoginRequiredMixin, UpdateView) :
    model = Store
    fields = ['title', 'address', 'content', 'table', 'head_image']

    template_name = 'store/store_update.html'

    def get_context_data(self, **kwargs) :
        context = super(StoreUpdate, self).get_context_data()
        return context

    def form_valid(self, form) :
        response = super(StoreUpdate, self).form_valid(form)
        return response

    def dispatch(self, request, *args, **kwargs) :
        if request.user.is_authenticated and request.user == self.get_object().author :
            return super(StoreUpdate, self).dispatch(request, *args, **kwargs)
        else :
            raise PermissionDenied

def new_Review(request, pk) :
    if request.user.is_authenticated :
        store = get_object_or_404(Store, pk=pk)

        if request.method == 'POST' :
            review_form = ReviewForm(request.POST)
            if review_form.is_valid() :
                review = review_form.save(commit=False)
                review.post = store
                review.author = request.user
                review.save()
                return redirect(review.get_absolute_url())
        else :
            return redirect(store.get_absolute_url())
    else :
        raise PermissionDenied