from django.urls import re_path
from complaints import views

urlpatterns=[
    re_path(r'^customer_post_complaint/(?P<idd>\w+)', views.customer_post_complaint,name='customer_post_complaint'),
    re_path(r'^customer_view_reply/', views.customer_view_reply,name='customer_view_reply'),
    re_path(r'^seller_post_reply/(?P<idd>\w+)', views.seller_post_reply,name='seller_post_reply'),
    re_path(r'^subseller_post_reply/(?P<idd>\w+)', views.subseller_post_reply,name='subseller_post_reply'),
    re_path(r'^subseller_view_complaints/', views.subseller_view_complaints,name='subseller_view_complaints'),
    re_path(r'^seller_view_complaints/', views.seller_view_complaints,name='seller_view_complaints')
]