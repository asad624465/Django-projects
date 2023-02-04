from django.urls import path 
from dashboard import views
app_name="dashboard"
urlpatterns = [
    path("home/",views.adminHome.as_view(), name="home"),
    path("product-list/",views.productList.as_view(), name="product-list"),
    path("add-new-product/",views.addNewProduct.as_view(), name="add-new-product"),
    path("update-product/<int:pk>",views.updateProduct.as_view(), name="update-product"),
    path("delete-product/<int:pk>",views.deleteProduct.as_view(), name="delete-product"),
    #start category path from here
    path("category-list/",views.categoryList.as_view(), name="category-list"),
    path("add-new-category/",views.addNewCategory.as_view(), name="add-new-category"),
    path("update-category/<int:pk>",views.updateCategory.as_view(), name="update-category"),
]
