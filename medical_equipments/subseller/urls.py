from django.urls import re_path
from subseller import views

urlpatterns=[
    re_path(r'^subseller_home/', views.subseller_home,name='subseller_home')      
]