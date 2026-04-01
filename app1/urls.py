from django.urls import path
# from .views import home
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/<int:pk>/', views.portfolio_details, name='portfolio_detail'),
]
