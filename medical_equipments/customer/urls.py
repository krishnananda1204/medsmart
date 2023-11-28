from django.urls import re_path
from customer import views

urlpatterns=[
    re_path(r'^registration/', views.registration,name='registration'),
    re_path(r'^customer_home/', views.customer_home,name='customer_home')
]