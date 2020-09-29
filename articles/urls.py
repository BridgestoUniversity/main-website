from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('', views.articles_page, name='articles-page'),
    path('<int:id>', views.articles_testing, name='testing'),
]
