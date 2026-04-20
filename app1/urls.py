from django.urls import path
# from .views import home
from . import views

# Baisc AUTH 
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/<int:pk>/', views.portfolio_details, name='portfolio_detail'),
    path('service/<slug:s_slug>/', views.service_details, name='service_detail'),

    # Default auth 
    # path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), )
    path('account/register/', views.register_user, name='register'),
    path('account/login/', views.login_user, name='login'),
    path('account/logout/', views.logout_user, name='logout'),
]
