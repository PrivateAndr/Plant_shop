from django.urls import path
from cart import views
from .cart import Cart


app_name = "cart"

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:plant_id>/', views.cart_add, name='cart_add'),
    path('update/<int:plant_id>/', views.cart_update, name='cart_update'),
    path('remove/<int:plant_id>/', views.cart_remove, name='cart_remove'),
]
