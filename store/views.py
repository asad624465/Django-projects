from multiprocessing import context
from django.shortcuts import render

from django.views.generic import ListView,DetailView
#load model for showing product in home page
from store.models import Product,Category

class ProductsList(ListView):
    model= Product
    template_name='frontend/index.html'
    context_object_name='products'

class productDetails(DetailView):
    model=Product
    template_name='frontend/product_details.html'
    context_object_name= 'item'
#def productDetails(req, id):
#    item = Product.objects.get(id=id)
#    context={'item':item}
#    return render(req,'frontend/product_details.html',context)
