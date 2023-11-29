from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import get_object_or_404

from django.db.models import Q

def list_product_controller(request):
    term = request.GET.get('term')
    
    all_products = Product.objects.all().order_by('-id')

    if term:
        all_products = all_products.filter(
            Q(title__icontains=term.strip()) |  # Filtra por título que contenha o termo (case-insensitive)
            Q(description__icontains=term.strip())  # Filtra por descrição que contenha o termo (case-insensitive)
        )

    all_categories = Category.objects.all().order_by('-id')

    return render(request, 'dashboard.view.html', {"all_products": all_products, 'all_categories': all_categories})


def product_details_controller(request, id):
    product = get_object_or_404(Product, id=id)
    all_categories = Category.objects.all().order_by('-id');
    return render(request,'detail.view.html', {'product': product, 'all_categories': all_categories})

def products_categories_controller(request, id):
    all_products = Product.objects.filter(category_id=id)
    all_categories = Category.objects.all().order_by('-id');
    return render(request,'dashboard.view.html', {'all_products': all_products, 'all_categories': all_categories})