from django.shortcuts import render
from .models import Product
# Create your views here.

def main_page(request):
    #products = Product.objects.all()
    return render(request, 'shop/main_page.html', {})
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/main_page.html', {'products' : products})