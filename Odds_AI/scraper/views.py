from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import os

# Selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def scrap(request):
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Firefox(options=options)

# Create your views here.

def view_name(request):
    return render(request, 'scraper.html', {})
