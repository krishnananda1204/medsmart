from django.urls import re_path
from product_order import views

urlpatterns=[
    re_path(r'^customer_manage_order/', views.customer_manage_order,name='customer_manage_order'),
    re_path(r'^seller_manage_order/', views.seller_manage_order,name='seller_manage_order'),
    re_path(r'^customer_view_order_history/', views.customer_view_order_history,name='customer_view_order_history'),
    re_path(r'^subseller_manage_order/', views.subseller_manage_order,name='subseller_manage_order'),    
    re_path(r'^subseller_accept_order/(?P<idd>\w+)', views.subseller_accept_order,name='subseller_accept_order'),
    re_path(r'^subseller_reject_order/(?P<idd>\w+)', views.subseller_reject_order,name='subseller_reject_order'),
    re_path(r'^seller_accept_order/(?P<idd>\w+)', views.seller_accept_order,name='seller_accept_order'),
    re_path(r'^seller_reject_order/(?P<idd>\w+)', views.seller_reject_order,name='seller_reject_order')
]


