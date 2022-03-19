from urllib import request
from django.contrib import admin
from django.urls import path, include
from scraper.views import DefaultView

urlpatterns = [
    path('scraper/', DefaultView.as_view(), name="scraper"),
]