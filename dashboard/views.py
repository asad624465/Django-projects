from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from store.models import Category,Product,ProductImage,VariationValue,Banner
from store.forms import *
from django.contrib import messages
#this is dashboard method
class adminHome(TemplateView):
    def get(self,request, *args, **kwargs):
        return render(request,'backend/home.html')
    
    def post(self,request, *args, **kwargs):
        pass
        
#product views
class productList(TemplateView):
    def get(self,request, *args, **kwargs):
        productList=Product.objects.all().order_by('-id')
        context={
            'productList':productList
        }
        return render(request,'backend/product/productlist.html',context)
    
    def post(self,request, *args, **kwargs):
        pass
#product views
class addNewProduct(TemplateView):
    def get(self,request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_type=='developer':
                categoryList=Category.objects.all().order_by('-id')
                context={
                    'categoryList':categoryList
                }
                return render(request,'backend/product/addProduct.html',context)
            else:
             return redirect('account:profile')    
        else:
           return redirect('store:index') 
    
    def post(self,request, *args, **kwargs):
        if request.user.user_type=='developer':
            if request.method=='post' or request.method=='POST':
                form = ProductForm(request.POST, request.FILES)
                if form.is_valid():
                    product=form.save(commit=False) 
                    slug=product.name.replace(' ','')
                    product.slug=slug
                    product.save()
                    messages.success(request, 'Your data has been successfully submitted!')
                    return redirect('dashboard:product-list') 
                else:
                    return redirect('dashboard:add-new-product') 
            else:
                return redirect('dashboard:add-new-product') 
        else:
            return redirect('dashboard:add-new-product')   

class updateProduct(TemplateView):   
    def get(self,request,pk,*args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_type=='developer':
                categoryList=Category.objects.all().order_by('-id')
                product_obj=Product.objects.get(id=pk)
                product=ProductForm(instance=product_obj)
                context={
                    'categoryList':categoryList,
                    'product':product,
                }
                return render(request,'backend/product/editProduct.html',context)
            else:
             return redirect('account:profile')    
        else:
           return redirect('store:index') 

    def post(self,request,pk, *args, **kwargs):
        if request.user.user_type=='developer':
            if request.method=='post' or request.method=='POST':
                product_obj=Product.objects.get(id=pk)
                form = ProductForm(request.POST, request.FILES,instance=product_obj)
                if form.is_valid():
                    product=form.save(commit=False) 
                    slug=product.name.replace(' ','')
                    product.slug=slug
                    product.save()
                    messages.success(request, 'Your data has been successfully updated!')
                    return redirect('dashboard:product-list') 
                else:
                    return redirect('dashboard:add-new-product') 
            else:
                return redirect('dashboard:add-new-product') 
        else:
            return redirect('dashboard:add-new-product')   
class deleteProduct(TemplateView): 
    def get(self,request,pk,*args, **kwargs):
        product=Product.objects.get(id=pk)
        product.delete()
        messages.success(request, 'You has been successfully removed data!')
        return redirect('dashboard:product-list') 

#start category info from here
class categoryList(TemplateView):
    def get(self,request,*args, **kwargs):
        categoryList=Category.objects.all().order_by('-id')
        context={
           'categoryList':categoryList 
        }
        return render(request,'backend/category/categoryList.html',context);
class addNewCategory(TemplateView):
    def get(self,request,*args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_type=='developer':
                categoryList=Category.objects.all().order_by('-id')
                context={
                    'categoryList':categoryList
                }
                return render(request,'backend/category/addCategory.html',context)
            else:
             return redirect('account:profile')    
        else:
           return redirect('store:index') 
    def post(self,request,*args, **kwargs):
        if request.method=='post' or request.method=='POST':
            form_obj=CategoryForm(request.POST, request.FILES)
            if form_obj.is_valid():
                form_obj.save()
                messages.success(request, 'Your data has been successfully updated!')
                return redirect('dashboard:category-list')
            else:
                messages.success(request, 'Sorry! You are not valid user!')
                return redirect('dashboard:category-list') 
        else:
            return redirect('store:index')     
            