
from django.contrib import admin
from django.urls import  path
from django.conf import settings
from django.conf.urls.static import static
# from django.urls import re_path
from django.urls import include, re_path
from django.views.generic.base import RedirectView
# from django.conf.urls import url

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)),
    re_path('cart/', include('cart.urls', namespace='cart')),
    re_path('orders/', include('orders.urls', namespace='orders')),
    re_path('', include('shop.urls', namespace='shop')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)