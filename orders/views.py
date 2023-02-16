from django.shortcuts import render, get_object_or_404
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from shop.models import Plant



# def cart_remove(request, plant_id):
#     cart= Cart(request)
#     plant = get_object_or_404(Plant, id=plant_id)
#     cart.remove(plant)
    

# def cart_clear(request):
#     cart = Cart(request)
#     for i in cart: return i.clear()

# def cart_delete_function(request):
#     cart = Cart(request)
#     plant = Plant.objects.get(id=request.GET.get('id'))
#     if cart:
#         cart.delete(plant)
#     else:
#         cart=Cart(request)
#         cart.save()
    
    # cart = Cart(request)
    # cart.clear()
    # print(cart)
    # return 0

# def cart_remove_function(request):
#     cart = Cart(request)
#     plant = get_object_or_404(Plant, id)
#     # for o in plant:
#     #     cart.remove(o)
#     print("==>> ",cart)
#     print("==>> ",plant)
    
# def cart_remove_function(request):
#     cart = Cart(request)
#     plant =Plant(id).all()
#     cart.remove(plant)


def order_create(request):
    
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        plant=item['plant'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # очистка корзины
            # cart = cart_clear(request).deleted()
            # # print("=====>",cart)
            # cart = int(0)
            # print(cart)
            # cart_clear(request)
            
            # cart = cart_clear(request)
            # print(("====> "),cart)
            # cart = cart_remove_function(request)a
            
            # cart= Cart(request)
            # plant = get_object_or_404(Plant, id=plant_id)
            # cart.remove(plant)
    
            
            
            
            cart.clear()
            # cart_remove(request)
            # cart.clear()
            # print(cart)
            # cart = Cart(request)
            # cart.save()
            # print("===>> ",cart)
            # cart_delete_function(request)
            # cart_remove_function(request)
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                {'cart': cart, 'form': form})
# Create your views here.

