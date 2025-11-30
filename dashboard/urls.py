from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard_home'),
    path('login/', views.dashboard_login, name='dashboard_login'),
    path('logout/', views.dashboard_logout, name='dashboard_logout'),

    # Orders
    path('orders/', views.orders_list, name='dashboard_orders'),
    path('orders/edit/<int:id>/', views.order_edit, name='dashboard_order_edit'),
    path('orders/delete/<int:id>/', views.order_delete, name='dashboard_order_delete'),
    path('orders/mark-delivered/<int:id>/', views.order_mark_delivered, name='dashboard_order_deliver'),


    # Products
    path('products/', views.products_list, name='dashboard_products'),
    path('products/add/', views.product_add, name='dashboard_product_add'),
    path('products/edit/<int:id>/', views.product_edit, name='dashboard_product_edit'),
    path('products/delete/<int:id>/', views.product_delete, name='dashboard_product_delete'),
]

