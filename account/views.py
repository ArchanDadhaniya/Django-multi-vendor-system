from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def registerUser(request):
    return HttpResponse("User registration page")

def registerRestaurant(request):
    return HttpResponse("Restaurant registration page")