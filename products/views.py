from django.shortcuts import render
from products.models import Product


# Create your views here.

def main(requests):
    if requests.method == 'GET':
        return render(requests, 'layouts/index.html')


def products_view(requests):
    if requests.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products
        }
        return render(requests, 'products/products.html', context=context)


def main_view(requests):
    if requests.method == 'GET':
        return render(requests, 'layouts/index.html')


def inproducts_view(requests):
    if requests.method == 'GET':
        return render(requests, 'products/products.html')
