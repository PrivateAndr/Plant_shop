from decimal import Decimal
from django.conf import settings
from shop.models import Plant
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Plant
from .forms import CartAddPlantForm


CART_SESSION_ID = 'cart'

class Cart(object):
    
    
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    
    def add(self, plant, quantity=1, update_quantity=False):
        plant_id = str(plant.id)
        if plant_id not in self.cart:
            self.cart[plant_id] = {'quantity':0,
                                'price': str(plant.price)}
        if update_quantity:
            self.cart[plant_id]['quantity'] = quantity
        else:
            self.cart[plant_id]['quantity'] += quantity
        self.save()
        
        
    def save(self):
        self.session.modified = True
        
        
    def remove(self, plant):
        plant_id = str(plant.id)
        if plant_id in self.cart:
            del self.cart[plant_id]
            self.save()
            
            
    def __iter__(self):
        plant_ids = self.cart.keys()
        plants = Plant.objects.filter(id__in=plant_ids)
        for plant in plants:
            self.cart[str(plant.id)]['plant'] = plant 
            
        for item in self.cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
            
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    
    def get_total_price(self):
       return sum(int(item['price']) * item['quantity'] for item in
            self.cart.values())
        
    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()

    def update_quantity(self, plant, quantity):
        plant_id = str(plant.id)
        if plant_id in self.cart:
            self.cart[plant_id]['quantity'] = quantity
            self.save()
