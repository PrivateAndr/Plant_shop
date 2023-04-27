# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Plant
from cart.forms import CartAddPlantForm


def plant_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    plants = Plant.objects.filter(available=True) 
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        plants = plants.filter(category=category)
    return render(request, 
                    'shop/plants/list.html',
                    {'category': category,
                    'categories': categories,
                    'plants': plants})
        
def plant_detail(request, id, slug):
    plant = get_object_or_404(Plant,
                              id=id,
                              slug=slug,
                              available=True)
    cart_plant_form = CartAddPlantForm()
    return render(request,
                  'shop/plants/detail.html',
                  {'plant': plant,
                   'cart_plant_form': cart_plant_form})