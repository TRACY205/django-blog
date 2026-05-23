from django.contrib import admin
from django.utils.html import mark_safe
from .models import Post, Category, Comment, Tag, PostTag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'status', 'published_at', 'views_count']
    list_filter = ['status', 'category', 'created_at', 'published_at']
    search_fields = ['title', 'content', 'author__username']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at', 'published_at', 'views_count', 'thumbnail_preview']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author', 'category')
        }),
        ('Content', {
            'fields': ('excerpt', 'content')
        }),
        ('Media', {
            'fields': ('featured_image', 'thumbnail_preview')
        }),
        ('Status & Publishing', {
            'fields': ('status', 'published_at')
        }),
        ('Statistics', {
            'fields': ('views_count', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def thumbnail_preview(self, obj):
        if obj.featured_image:
            return mark_safe(f'<img src="{obj.featured_image.url}" width="300" />')
        return "No image"
    thumbnail_preview.short_description = 'Image Preview'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'is_approved', 'created_at']
    list_filter = ['is_approved', 'created_at']
    search_fields = ['author', 'email', 'post__title']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Comment Details', {
            'fields': ('post', 'author', 'email')
        }),
        ('Content', {
            'fields': ('content',)
        }),
        ('Approval', {
            'fields': ('is_approved',)
        }),
        ('Meta', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    list_display = ['post', 'tag']
    list_filter = ['tag']
    search_fields = ['post__title', 'tag__name']
