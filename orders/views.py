from django.shortcuts import render, get_object_or_404
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from shop.models import Plant


@login_required(login_url='login')  # Вимагаємо аутентифікацію для доступу до сторінки
def order_create(request):
    cart = Cart(request)
    cart_list_db = request.session.get('cart', {})  # Отримуємо дані кошика з сесії

    if len(cart_list_db) == 0:  # Перевіряємо кількість товарів у кошику
        messages.error(request, "Your cart is empty. Add items to your cart before placing an order.")
        return redirect('shop:plant_list')  # Перенаправляємо на сторінку зі списком товарів

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user  # Призначення поточного користувача
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                            plant=item['plant'],
                                            price=item['price'],
                                            quantity=item['quantity'])
            order.total_cost = cart.get_total_price()
            order.save()
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        if request.user.is_authenticated:  # Перевіряємо, чи користувач увійшов в систему
            initial_data = {'first_name': request.user.first_name, 'last_name': request.user.last_name}
            form = OrderCreateForm(initial=initial_data)
        else:
            form = OrderCreateForm()

    login_register_url = 'login'  # URL для сторінки входу/реєстрації
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form, 'login_register_url': login_register_url})


