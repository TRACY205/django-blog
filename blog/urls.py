from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('all/', views.all_posts, name='all-posts'),
    path('search/', views.search_posts, name='search'),
    path('category/<slug:slug>/', views.category_posts, name='category-posts'),
    path('tag/<slug:slug>/', views.tag_posts, name='tag-posts'),
    path('post/<slug:slug>/', views.post_detail, name='post-detail'),
]