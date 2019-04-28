from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from basketapp.models import Basket

def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []

def get_hot_product():
    return Product.objects.all().order_by('?').first()


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]

    return same_products


def main(request):
    basket = get_basket(request.user)
    context = {
        'basket': basket,
    }

    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    basket = get_basket(request.user)

    if pk:
        if pk == '0':
            category = {'name': 'All'}
            product_list = Product.objects.all()
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            product_list = Product.objects.filter(category=category.id)

        context = {
            'title': 'Products',
            'links_menu': links_menu,
            'products': product_list,
            'category': category,
            'basket': basket,
        }
        return render(request, 'mainapp/product_list.html', context)
    else:
        product_list = Product.objects.all()

        hot_product = get_hot_product()
        same_products = get_same_products(hot_product)

        context = {
            'title': 'Продукты',
            'links_menu': links_menu,
            'hot_product': hot_product,
            'same_products': same_products,
            'basket': basket,
        }
        return render(request, 'mainapp/products.html', context)


def product(request, pk):
    title = 'Product'

    context = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user)
    }

    return render(request, 'mainapp/product.html', context)


def contacts(request):
    basket = get_basket(request.user)
    context = {
        'basket': basket,
    }
    return render(request, 'mainapp/contacts.html', context)
