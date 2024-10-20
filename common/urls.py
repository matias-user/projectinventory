from django.urls import path
from .views import home
from django.contrib.auth import views as auth_views

app_name = 'common'
urlpatterns = [
    path('', home, name='home' ),
    path ('login/', auth_views.LoginView.as_view(), name='login')

]
