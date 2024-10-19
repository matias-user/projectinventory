from django.urls import path
from .views import create_or_update_product

app_name= 'inventory'
urlpatterns = [
    path('create/', create_or_update_product, name='create' ),
    path('update/<product_id>/', create_or_update_product, name='update' ),
]
