from django.urls import path
from .views.inventory_views import home

urlpatterns = [
    path('', home, name='home' ),
]
