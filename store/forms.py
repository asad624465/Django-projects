from django.forms.models import ModelForm 
from store.models import Product,Category

class ProductForm(ModelForm):
    
    class Meta:
        model = Product
        fields = ('name','category','preview_desc','description','images','price','old_price','is_stock')

#start category from here
class CategoryForm(ModelForm):
    
    class Meta:
        model = Category
        fields = ('name','parent','image')
