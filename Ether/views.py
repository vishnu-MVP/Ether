from django.shortcuts import render
from store.models import Product,ReviewRating
def home(request):
    products = Product.objects.all().filter(is_available=True)
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)

    context ={
        'products' : products,
        'reviews': reviews,
    }


    return render(request,'home.html', context)

def pp(request):
    return render(request,'privacy.html')

def tc(request):
    return render(request,'tandc.html')
def cr(request):
    return render(request,'crp.html')
