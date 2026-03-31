from django.urls import path
# from .views import home
from . import views

urlpatterns = [
    path('all', views.blog_index, name='blog-index'),
]
