from django.urls import path
from store import views
app_name='store'

urlpatterns = [
    path('',views.ProductsList.as_view(),name='index'),
    path('product/<slug>/',views.productDetails.as_view(),name='product-details'),
]