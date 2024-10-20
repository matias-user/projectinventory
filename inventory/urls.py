from django.urls import path
from .views import create_or_update_product, list_products

app_name= 'inventory'
urlpatterns = [
    path('create/', create_or_update_product, name='create' ),
    path('update/<product_id>/', create_or_update_product, name='update' ),
    path('', list_products, name='products' )
]
