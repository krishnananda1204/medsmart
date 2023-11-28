from django.urls import re_path
from seller import views

urlpatterns=[
   re_path(r'^seller_home/', views.seller_home,name='seller_home')      
]