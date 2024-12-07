from django.urls import path
from home_screen import views

urlpatterns = [
    path('home', views.home_screen_info),
    path('get_all_state', views.get_state_logic),
    path('get_district', views.get_district_logic),
    path('get_organizations', views.get_organizations_logic),
    path('product_info', views.product_info),
    path('product_list', views.home_sub_category_product_info),
    path('product_info_list', views.product_info_list),
    path('address', views.address_operation),
    path('search', views.search_functionality),
    path('photo_upload', views.upload_image),  
    path('category_info', views.Category_info),
    path('update_rating', views.rating_update), 
    path('start_stop', views.start_stop), 
]
