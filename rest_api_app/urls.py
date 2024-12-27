from django.contrib import admin
from django.urls import path, include
from rest_api_app.views import category_list_api, product_list_api, product_reviews, review_list

urlpatterns = [
    path('api/categories/', category_list_api, name='category_list_api'),
    path('api/products/', product_list_api, name='product_list_api'),
    path('products/<int:product_id>/reviews/', product_reviews, name='product_reviews'),
    path('api/products/<int:product_id>/reviews/', review_list, name='review_list'),
]