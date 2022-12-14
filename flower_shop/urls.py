
from django.contrib import admin
from django.urls import  path
from django.conf import settings
from django.conf.urls.static import static
# from django.urls import re_path
from django.urls import include, re_path
# from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('shop.urls', namespace='shop')),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)