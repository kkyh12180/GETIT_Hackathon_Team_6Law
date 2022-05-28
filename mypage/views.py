from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.

def mypage(request) :

    return render (
        request, 
        'mypage/mypage.html', 
    )
