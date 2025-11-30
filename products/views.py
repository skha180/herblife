from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order
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

