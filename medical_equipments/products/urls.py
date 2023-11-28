from django.urls import re_path
from products import views

urlpatterns=[
    re_path(r'^customer_search_product/', views.customer_search_product,name='customer_search_product'),
    re_path(r'^seller_manage_products/', views.seller_manage_products,name='seller_manage_products'),
    re_path(r'^seller_reg_products/', views.seller_reg_products,name='seller_reg_products'),      
    re_path(r'^subseller_manage_products/', views.subseller_manage_products,name='subseller_manage_products'),
    re_path(r'^subseller_reg_products/', views.subseller_reg_products,name='subseller_reg_products'),
    re_path(r'^subseller_update_product_details/(?P<idd>\w+)', views.subseller_update_product_details,name='subseller_update_product_details'),
    re_path(r'^subseller_update_stock/(?P<idd>\w+)', views.subseller_update_stock,name='subseller_update_stock'),
    re_path(r'^seller_update_stock/(?P<idd>\w+)', views.seller_update_stock,name='seller_update_stock'),
    re_path(r'^subseller_delete_product/(?P<idd>\w+)', views.subseller_delete_product,name='subseller_delete_product'),
    re_path(r'^seller_delete_product/(?P<idd>\w+)', views.seller_delete_product,name='seller_delete_product'),
    re_path(r'^seller_update_product_details/(?P<idd>\w+)', views.seller_update_product_details,name='seller_update_product_details')
]