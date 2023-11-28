from django.urls import re_path
from cart import views

urlpatterns=[
    re_path(r'^add_to_cart/(?P<idd>\w+)', views.add_to_cart,name='add_to_cart'),
    re_path(r'^view_cart/', views.view_cart,name='view_cart'),
    re_path(r'^customer_place_order/(?P<idd>\w+)', views.customer_place_order,name='customer_place_order')
]