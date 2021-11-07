from django.urls import path
from base.views import order_views as views

urlpatterns = [
    path('add/', views.addOrderItems, name='orders-add'),
    path('myorders/', views.getMyOrders, name='myorders'),
    path('orders/', views.getOrders, name='orders'),
    path('<str:pk>/', views.getOrderById, name='user-order'),
    path('<str:pk>/pay/', views.updateOrdertoPaid, name='pay'),
    path('<str:pk>/deliver/', views.updateOrdertoDelivered, name='deliver')
]
