from django.urls import path
from notification import views
app_name='notifac'

urlpatterns = [
    path('is_read/<int:pk>/', views.seenNotification, name='is_read'),
]