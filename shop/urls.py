from django.urls import path
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static

# from django.conf.urls import url

from . import views

app_name = 'shop'

urlpatterns = [
    re_path(r'^$', views.plant_list, name='plant_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.plant_list, name='plant_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.plant_detail, name='plant_detail'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
