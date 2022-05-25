from django.urls import path
from . import views

urlpatterns = [
    path('', views.StoreList.as_view()), 
    path('<int:pk>/', views.StoreDetail.as_view()),
    path('<int:pk>/new_review/', views.new_Review),
    path('update_store/<int:pk>/', views.StoreUpdate.as_view()),
]