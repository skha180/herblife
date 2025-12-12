from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),              # NEW HOME PAGE
    path('products/', views.product_list, name='product_list'),
    path('order/<int:product_id>/', views.order_create, name='order_create'),
    path('order/success/', views.order_success, name='order_success'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Dynamic blog page for each product
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
]
