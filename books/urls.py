from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='books-home'),
    path('books/', views.all, name='books-all'),
    path('books/<int:id>/', views.show, name='books-show'),
    path('books/new/', views.create, name='books-create')
]

