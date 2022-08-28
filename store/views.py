from django.shortcuts import render

from django.views.generic import ListView,DetailView

def home(req):
    return render(req,'frontend/index.html')
