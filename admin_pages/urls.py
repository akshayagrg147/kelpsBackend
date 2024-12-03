from django.urls import path
from . import views

urlpatterns = [
    path('category', views.Category.as_view()),
    path('sub_category', views.Sub_Category.as_view()),
    path('organization', views.Organisation.as_view()),
    path('products', views.Products.as_view()),
    path('search_product', views.product_search),
    path('search_organization', views.organization_search),
    path('search_sub_category', views.sub_category_search),
    path('search_category', views.category_search),
    path('category_info', views.Category_info),
    path('product_info', views.product_info)
]
