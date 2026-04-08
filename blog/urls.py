from django.urls import path
# from .views import home
from . import views

urlpatterns = [
    path('all', views.blog_index, name='blog-index'),
    path('<uuid:blog_id>', views.blog_detail, name='blog-detail'),
]
