from django.conf.urls import url

from . import views

app_name = 'catalogue'
urlpatterns = [
    url(r'^$', views.Product1View, name='lis1'),
    url(r'^(?P<product_id>[0-9]+)/$', views.product_detail, name='detail'),
    ]