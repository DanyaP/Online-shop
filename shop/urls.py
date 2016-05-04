from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^product_list$', views.product_list, name='product_list'),
    url(r'^product/([0-9]+)$', views.product_view, name='product_view'),
    #url(r'^images$', views.images, name='images'),
]