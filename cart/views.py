from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from shop.models import Plant
from .cart import Cart

from .forms import CartAddPlantForm



@require_POST
def cart_add(request, plant_id):
    cart = Cart(request)
    plant = get_object_or_404(Plant, id=plant_id)
    form = CartAddPlantForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(plant=plant, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


@require_POST
def cart_update(request, plant_id):
    cart = Cart(request)
    plant = get_object_or_404(Plant, id=plant_id)
    form = CartAddPlantForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.update_quantity(plant=plant, quantity=cd['quantity'])
    return redirect('cart:cart_detail')


def cart_remove(request, plant_id):
    cart = Cart(request)
    plant = get_object_or_404(Plant, id=plant_id)
    cart.remove(plant)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        form = CartAddPlantForm(initial={'quantity': item['quantity'], 'update': True})
        item['update_quantity_form'] = form
    return render(request, 'cart/detail.html', {'cart': cart})


@require_POST
def cart_update(request, plant_id):
    cart = Cart(request)
    plant = get_object_or_404(Plant, id=plant_id)
    form = CartAddPlantForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.update_quantity(plant=plant, quantity=cd['quantity'])
    return redirect('cart:cart_detail')