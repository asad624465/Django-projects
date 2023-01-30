from django.forms.models import ModelForm 
from store.models import Product

class ProductForm(ModelForm):
    
    class Meta:
        model = Product
        fields = ('name','category','preview_desc','description','images','price','old_price','is_stock')
