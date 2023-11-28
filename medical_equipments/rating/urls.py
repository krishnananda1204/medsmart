from django.urls import re_path
from rating import views

urlpatterns=[
    re_path(r'^customer_add_rating/(?P<idd>\w+)', views.customer_add_rating,name='customer_add_rating'),      
    re_path(r'^seller_view_ratings/', views.seller_view_ratings,name='seller_view_ratings'),
    re_path(r'^subseller_view_ratings/', views.subseller_view_ratings,name='subseller_view_ratings')      
]