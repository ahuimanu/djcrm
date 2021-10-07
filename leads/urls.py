from django.contrib import admin
from django.urls import path

from . import views

app_name = "leads"

urlpatterns = [
    path('', views.home_page, name='leads_home_page'),
]
