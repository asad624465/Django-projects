from django.shortcuts import render

from django.views.generic import ListView,DetailView
#load model for showing product in home page
from store.models import Product,Category

class ProductsList(ListView):
    model= Product
    template_name='frontend/index.html'
    context_object_name='products'
