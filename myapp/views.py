from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/dashboard.html')

def cart(request):
    return render(request, 'pages/cart.html')

def shop(request):
    return render(request, 'pages/shop.html')

def product(request):
    return render(request, 'pages/single-product.html')

def checkout(request):
    return render(request, 'pages/checkout.html')