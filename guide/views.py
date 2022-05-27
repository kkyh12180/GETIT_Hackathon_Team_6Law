from django.shortcuts import render

# Create your views here.

def show_guide(request) :
    return render (
        request, 
        'guide/guide.html', 
    )