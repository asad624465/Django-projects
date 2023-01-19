from django.urls import path
from account import views

app_name='account'

urlpatterns = [
    path('register/', views.register,name='register'),
    path('login/', views.Customerlogin,name='login'),
    path("profile/", views.profileViews.as_view(), name="profile"),
    path("my-billing-information/", views.myBillingInfo.as_view(), name="my-billing-information"),
    path("my-account-information/", views.myAccountInfo.as_view(), name="my-account-information")
]
