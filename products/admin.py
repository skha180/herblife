from django.contrib import admin
from .models import Product, Order, BlogPost  # <-- import BlogPost

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ('title',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'phone', 'address', 'created_at')
    search_fields = ('name', 'phone', 'product__title')

# --- Register BlogPost ---
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'product', 'author', 'created_at', 'is_active')
    search_fields = ('title', 'product__title', 'author')
    list_filter = ('is_active', 'created_at', 'product')
    prepopulated_fields = {"slug": ("title",)}  # automatically fills slug from title
