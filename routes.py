from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ListAllProducts.as_view(), name='list_all_products'),
    path('products/<int:pk>/', views.ReadUpdateDeleteProduct.as_view(), name='read_update_delete_product'),
    path('products/name/<str:name>/', views.ListByName.as_view(), name='list_by_name'),
    path('products/category/<str:category>/', views.ListByCategory.as_view(), name='list_by_category'),
    path('products/availability/<str:availability>/', views.ListByAvailability.as_view(), name='list_by_availability'),
]
