from django.urls import path
from order import views
app_name='order'

urlpatterns = [
   path('add-to-cart/<int:pk>', views.addToCart, name='add-to-cart'),
   path('cart-view/', views.cartView, name='cart'),
]