from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='book-index'),
    path('<int:book_id>', views.show, name='show-book'),
    path('new/', views.create, name='book-create')
]