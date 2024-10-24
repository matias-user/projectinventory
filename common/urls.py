from django.urls import path
from .views import home, create_user
from django.contrib.auth import views as auth_views

app_name = 'common'
urlpatterns = [
    path('', home, name='home' ),
    path ('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout' ),
    path('registrate/',  create_user, name='register')

]
