from multiprocessing import context
from django.shortcuts import render

from django.views.generic import ListView,DetailView,TemplateView
#load model for showing product in home page
from store.models import Product,Category,ProductImage,Banner

class ProductsList(TemplateView):
    def get(self,request,*args, **kwargs):
        products=Product.objects.all().order_by('-id')
        banners=Banner.objects.filter(is_active=True).order_by('-id')[0:3]
        context={'products':products,'banners':banners}
        return render(request,'frontend/index.html',context);

    def post(self,request,*args, **kwargs):
        if request.method=="POST" or request.method=="post":
            name=request.POST.get('item')
            products=Product.objects.filter(name__icontains=name).order_by('-id')
            context={'products':products,'banners':''}
            return render(request,'frontend/index.html',context);
            
    
class productDetails(DetailView):
    model=Product
    template_name='frontend/product_details.html'
    context_object_name= 'item'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['product_images'] = ProductImage.objects.filter(product=self.object.id)
        return context

#def productDetails(req, id):
#    item = Product.objects.get(id=id)
#    photos=ProductImage.objects.filter(product=item).order_by('-createdate')
#    context={'item':item,'photos':photos}
#    return render(req,'frontend/product_details.html',context)
