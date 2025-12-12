from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, BlogPost
from .forms import OrderForm


def home(request):
    products = Product.objects.all()[:3]  # show 3 sample products
    return render(request, 'home.html', {'products': products})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def order_create(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            # Redirect to a thank you page or WhatsApp redirect
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'products/order_form.html', {'form': form, 'product': product})


def order_success(request):
    return render(request, 'products/order_success.html')


def about(request):
    return render(request, 'products/about.html')


def contact(request):
    return render(request, 'products/contact.html')


# --- New view for blog detail ---
from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Product

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_active=True)
    product = post.product

    # Dummy data for testing comments and bloggers
    comments = [
        {"name": "Alice", "text": "Great product!", "date": "2025-12-01", "likes": 5, "avatar": product.image},
        {"name": "Bob", "text": "I love it!", "date": "2025-12-02", "likes": 3, "avatar": product.image},
    ]
    bloggers = [
        {"avatar": product.image},
        {"avatar": product.image},
    ]
    other_count = 2

    # Example cities for order form dropdown
    cities = ["New York", "London", "Paris", "Berlin"]

    return render(request, 'products/blog_detail.html', {
        "post": post,
        "product": product,
        "comments": comments,
        "bloggers": bloggers,
        "other_count": other_count,
        "cities": cities,
        "landing_url": "#",  # replace with actual landing URL if needed
    })
