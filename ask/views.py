
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post, Category, Answer
from .forms import AnswerForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied


# Create your views here.

class PostList(ListView) :
    model = Post
    ordering = '-pk'
    template_name = 'ask/ask_list.html'

    def get_context_data(self, **kwargs) :
        context = super(PostList, self).get_context_data()
        return context

class PostDetail(DetailView) :
    model = Post
    template_name = 'ask/ask_detail.html'

    def get_context_data(self, **kwargs) :
        context = super(PostDetail, self).get_context_data()
        context['comment_form'] = AnswerForm
        return context

class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'file_upload','category']
    template_name = 'ask/ask_form.html'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/ask/')

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'file_upload', 'category']
    template_name = 'ask/post_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

def category_page(request, slug):
    if slug == 'no category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'ask/ask_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category': category,
        }
    )    

def new_answer(request, pk) :
    if request.user.is_authenticated :
        post = get_object_or_404(Post, pk=pk)

        if request.method == 'POST' :
            answer_form = AnswerForm(request.POST)
            if answer_form.is_valid() :
                answer = answer_form.save(commit=False)
                answer.post = post
                answer.author = request.user
                answer.save()
                return redirect(answer.get_absolute_url())
        else :
            return redirect(post.get_absolute_url())
    else :
        raise PermissionDenied