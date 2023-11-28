from django.urls import re_path
from payment import views

urlpatterns=[
     re_path(r'^seller_view_payments/', views.seller_view_payments,name='seller_view_payments'),
     re_path(r'^subseller_view_payments/', views.subseller_view_payments,name='subseller_view_payments'),
     re_path(r'^customer_add_payment/', views.customer_add_payment,name='customer_add_payment'),
     re_path(r'^add_payment/(?P<idd>\w+)', views.add_payment,name='add_payment')     
]     