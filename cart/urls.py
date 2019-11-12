from django.conf.urls import url
from . import views

app_name = 'cart'

urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
    url(r'^formular(?P<person_id>\d+)/$', views.formular, name="formular"),
    url(r'^formular_submit(?P<person_id>\d+)/$', views.formular_submit, name="formular_submit"),
]