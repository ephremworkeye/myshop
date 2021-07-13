from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.

def product_list(request, cat_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all(available=True)
    if cat_slug:
        category = get_object_or_404(Category, slug=cat_slug)
        products.filter(category=category)
        return render(request, 'shop/product/list.html', {'category':category, 'categories':categories, 'products':products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product':product})
    