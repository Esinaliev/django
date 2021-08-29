from django.shortcuts import render, get_object_or_404

from mainapp.models import Product, ProductCategory
from basketapp.models import Basket


def products(request, pk=None):
    title = "продукт | каталог"

    links_menu = ProductCategory.objects.all()
    products_all = Product.objects.all().order_by('price')

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'links_menu': links_menu,
        'products_all': products_all,
        'basket': basket,
    }

    if pk is not None:
        if pk == 0:
            products_all = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_all = Product.objects.filter(category__pk=pk).order_by('price')

        context['category'] = category
        context['products_all'] = products_all

    return render(request=request, template_name='mainapp/products.html', context=context)


def product(request, pk):
    title = "продукт"

    current_product = get_object_or_404(Product, pk=pk)
    products_all = Product.objects.filter(category__pk=current_product.category.pk).exclude(pk=current_product.pk).order_by('price')[:12]

    context = {
        'title': title,
        'current_product': current_product,
        'products_all': products_all,
    }

    return render(request=request, template_name='mainapp/product.html', context=context)
