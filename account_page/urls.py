from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout), 
    path('login/', views.login_page), 
    path('signup/', views.signup_page),  
    path('do_login/', views.login, name='login'),
    path('do_signup/', views.signup, name='signup'),
]