"""medical_equipments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path
from django.conf.urls import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from login import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'^cart/',include('cart.urls')),
    re_path(r'^complaints/',include('complaints.urls')),
    re_path(r'^customer/',include('customer.urls')),
    re_path(r'^login/',include('login.urls')),
    re_path(r'^payment/',include('payment.urls')),
    re_path(r'^product_order/',include('product_order.urls')),
    re_path(r'^products/',include('products.urls')),
    re_path(r'^rating/',include('rating.urls')),
    re_path(r'^seller/',include('seller.urls')),
    re_path(r'^stock/',include('stock.urls')),
    re_path(r'^subseller/',include('subseller.urls')),
    re_path('$',views.login)
]

urlpatterns+=staticfiles_urlpatterns()
