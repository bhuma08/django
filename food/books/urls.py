from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='book-index'),
    path('<int:book_id>', views.show, name='show-book')
]