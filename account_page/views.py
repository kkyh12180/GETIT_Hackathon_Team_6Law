from django.shortcuts import redirect, render
from .models import User
from django.contrib import auth

# Create your views here.
def login_page(request) :
    return render (
        request, 
        'account_page/login.html', 
    )

def signup_page(request) :
    return render (
        request, 
        'account_page/signup.html', 
    )

def login(request) :
    if request.method == "POST" :
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, username=email, password=password)
        if user is not None :
            auth.login(request, user)
            return redirect('/store')
        else :
            return render(request, 'login.html', {'error' : 'e-mail or password is incorrect.'})
    else :
        return render(request, 'login.html')

def signup(request) :
    if request.method == "POST" :
        if request.POST["password"] == request.POST['check_password'] :
            user = User.objects.create_user(
                email = request.POST['email'],
                nickname = request.POST['nickname'],
                password = request.POST['password'],
                date_of_birth = request.POST['date_of_birth'],
                is_seller = request.POST['is_seller'],
            )
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/store')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

def logout(request) :
    auth.logout(request)
    return redirect('/')