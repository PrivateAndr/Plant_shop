from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from orders.models import Order
from orders.models import OrderItem
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/registration/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            messages.success(request, 'Регистрация прошла успешно. Войдите в свой аккаунт.')
            return render(request, 'account/registration/register_done.html', {'user_form': user_form})
        else:
            messages.error(request, 'Ошибка регистрации. Пожалуйста, исправьте ошибки в форме.')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/registration/register.html', {'user_form': user_form})


def orders(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    return render(request, 'account/orders/orders.html', {'user': user, 'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'account/orders/order_detail.html', {'order': order})

@login_required
def profile(request):
    user = request.user
    return render(request, 'account/profile/profile.html', {'user': user})