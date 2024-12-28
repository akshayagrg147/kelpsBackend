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
    path('verify_payment', views.verify_payment),
    path('admin_orders_details', views.admin_orders_details),
    path('sales_overview', views.sales_overview_logic),
    path('order_status_wise', views.order_status_wise_logic),
    path('order_by_status', views.order_by_status_logic),
]

