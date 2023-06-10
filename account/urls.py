from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView,redirect_to_login

from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import LogoutThenLoginView



urlpatterns = [
    # path('signup/', views.signup, name='signup'),
    path(r'login/', LoginView.as_view(template_name='account/registration/login.html'), name='login'),
    # path('logout/', views.logout_view, name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('logout-then-login/', redirect_to_login.as_view(login_url='account/registration/signuo.html'), name='logout_then_login'),
    # path('logout-then-login/', LogoutThenLoginView.as_view(), name='logout_then_login'),
    path('', views.dashboard, name='dashboard'),

    path('register/', views.register, name='register'),

    path('orders/', views.orders, name='orders'),  # URL для перегляду всіх замовлень
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),  # URL для перегляду окремого замовлення

    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('profile/', views.profile, name='profile'),

]
