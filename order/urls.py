from django.urls import path
from order import views

urlpatterns = [
    path('order_history', views.order_history),
    path('place_order', views.order_place),
    path('order_details', views.order_details),
    path('order_status_update', views.order_status),
    path('order_list', views.order_list),
    path('order_stats', views.order_stats),
    path('search_order', views.order_search),
    path('verify_payment', views.verify_payment)
]
