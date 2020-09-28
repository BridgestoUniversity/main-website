from django.contrib import admin
from django.urls import path
from about import views

urlpatterns = [
    path('', views.about_page, name='about-page'),
    path('our-team', views.our_team, name='our-team'),
    path('get-involved', views.get_involved, name='get-involved')
]
