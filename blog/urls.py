from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.blog_list, name='blogs'),
    path('blogs/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
