from django.urls import path
from order import views
app_name='order'

urlpatterns = [
   path('add-to-cart/<int:pk>', views.addToCart, name='add-to-cart'),
   path('cart-view/', views.cartView, name='cart'),
   path("remove-item/<int:pk>",views.removeItemFromCart, name='remove-item'),
   path("increase-item/<int:pk>", views.increaseItemOfCart, name='increase-item'),
   path("decrease-item/<int:pk>", views.decreaseItemOfCart, name='decrease-item'),
]