from django.urls import path, include
from . import views


urlpatterns = [
    path('registerUser/', views.registerUser, name='registerUser'),
    path('registerRestaurant/', views.registerRestaurant, name='registerRestaurant'),
]