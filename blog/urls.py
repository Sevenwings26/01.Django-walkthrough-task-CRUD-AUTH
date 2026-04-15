from django.urls import path
# from .views import home
from . import views

urlpatterns = [
    path('all', views.blog_index, name='blog-index'),
    path('<uuid:blog_id>', views.blog_detail, name='blog-detail'),
    path('create', views.blog_create, name='blog-create'),
    path('blog/<uuid:id>/update/', views.blog_update, name='blog-update'),
    path('blog/<uuid:id>/delete/', views.blog_delete, name='blog-delete'),
]
