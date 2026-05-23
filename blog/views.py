from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Post, Category, Tag, Comment


# Homepage - List all published posts
def home(request):
    posts = Post.objects.filter(status='published')
    categories = Category.objects.all()
    featured_post = posts.first() if posts else None
    
    context = {
        'posts': posts,
        'categories': categories,
        'featured_post': featured_post,
    }
    return render(request, 'blog/index.html', context)


# Category view - Posts in a specific category
def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, status='published')
    categories = Category.objects.all()
    
    context = {
        'posts': posts,
        'category': category,
        'categories': categories,
    }
    return render(request, 'blog/category.html', context)


# Tag view - Posts with a specific tag
def tag_posts(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags__tag=tag, status='published').distinct()
    categories = Category.objects.all()
    
    context = {
        'posts': posts,
        'tag': tag,
        'categories': categories,
    }
    return render(request, 'blog/tag.html', context)


# Post detail view
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    post.views_count += 1
    post.save()
    
    approved_comments = post.comments.filter(is_approved=True)
    categories = Category.objects.all()
    related_posts = Post.objects.filter(
        category=post.category,
        status='published'
    ).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'comments': approved_comments,
        'categories': categories,
        'related_posts': related_posts,
    }
    return render(request, 'blog/post_detail.html', context)


# Search view
def search_posts(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(status='published')
    categories = Category.objects.all()
    
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(excerpt__icontains=query)
        )
    
    context = {
        'posts': posts,
        'query': query,
        'categories': categories,
    }
    return render(request, 'blog/search.html', context)


# All posts view
def all_posts(request):
    posts = Post.objects.filter(status='published')
    categories = Category.objects.all()
    
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'blog/all_posts.html', context)
