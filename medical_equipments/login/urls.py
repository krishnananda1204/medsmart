from django.urls import re_path
from login import views

urlpatterns=[
    re_path(r'^login/', views.login,name='login')
]
