from django.urls import re_path
from stock import views

urlpatterns=[
  re_path(r'^update_stock/', views.update_stock,name='update_stock')      
]