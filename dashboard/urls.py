from django.urls import path 
from dashboard import views

urlpatterns = [
    path("home/",views.adminHome.as_view(), name="home")
]
