from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from products.models import Order, Product
from products.forms import OrderForm, ProductForm


# ------------------ REUSABLE FILTER FUNCTION ------------------
def filter_orders(request, queryset):
    status = request.GET.get('status')
    search = request.GET.get('q')

    if status:
        queryset = queryset.filter(status=status)
    if search:
        queryset = queryset.filter(name__icontains=search)

    return queryset


# ------------------ DASHBOARD HOME ------------------
@login_required(login_url='dashboard_login')
def home(request):
    orders = filter_orders(request, Order.objects.order_by('-created_at'))

    paginator = Paginator(orders, 5)
    page = request.GET.get('page')
    orders = paginator.get_page(page)

    total_orders = Order.objects.count()
    total_products = Product.objects.count()

    # ---- Chart Data (Safe) ----
    if orders:
        chart_labels = [o.created_at.strftime("%d %b") for o in orders][::-1]
        chart_data = [
            Order.objects.filter(created_at__date=o.created_at.date()).count()
            for o in orders
        ][::-1]
    else:
        chart_labels, chart_data = [], []

    products_labels = [p.title for p in Product.objects.all()]
    products_data = [p.order_set.count() for p in Product.objects.all()]

    return render(request, 'dashboard/home.html', {
        'orders': orders,
        'total_orders': total_orders,
        'total_products': total_products,
        'chart_labels': chart_labels,
        'chart_data': chart_data,
        'products_labels': products_labels,
        'products_data': products_data,
    })


# ------------------ ORDERS LIST ------------------
@login_required(login_url='dashboard_login')
def orders_list(request):
    orders = filter_orders(request, Order.objects.order_by('-created_at'))

    paginator = Paginator(orders, 10)
    page_number = request.GET.get('page')
    orders = paginator.get_page(page_number)

    return render(request, 'dashboard/orders_list.html', {
        'orders': orders,
        'status_filter': request.GET.get('status'),
        'search_query': request.GET.get('q'),
    })


# ------------------ ORDER EDIT ------------------
@login_required(login_url='dashboard_login')
def order_edit(request, id):
    order = get_object_or_404(Order, id=id)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, "Order updated successfully!")
            return redirect('dashboard_orders')
    else:
        form = OrderForm(instance=order)

    return render(request, 'dashboard/order_edit.html', {
        'form': form,
        'order': order,
    })


# ------------------ ORDER DELETE ------------------
@login_required(login_url='dashboard_login')
def order_delete(request, id):
    order = get_object_or_404(Order, id=id)
    order.delete()
    messages.error(request, "Order deleted!")
    return redirect('dashboard_orders')


# ------------------ PRODUCTS LIST ------------------
@login_required(login_url='dashboard_login')
def products_list(request):
    products = Product.objects.all()

    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'dashboard/products_list.html', {
        'products': products,
    })


# ------------------ PRODUCT EDIT ------------------
@login_required(login_url='dashboard_login')
def product_edit(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully!")
            return redirect('dashboard_products')
    else:
        form = ProductForm(instance=product)

    return render(request, 'dashboard/product_edit.html', {
        'form': form,
        'product': product,
    })


@login_required(login_url='dashboard_login')
def order_mark_delivered(request, id):
    order = get_object_or_404(Order, id=id)
    order.status = "delivered"  # mark as delivered
    order.save()
    messages.success(request, f"Order #{order.id} marked as delivered!")
    return redirect('dashboard_orders')


@login_required(login_url='dashboard_login')
def product_add(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully!")
            return redirect('dashboard_products')
    else:
        form = ProductForm()

    return render(request, 'dashboard/product_edit.html', {
        'form': form,
        'product': None,
    })



# ------------------ PRODUCT DELETE ------------------
@login_required(login_url='dashboard_login')
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.error(request, "Product deleted!")
    return redirect('dashboard_products')




# Login View
def dashboard_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard_home')  # redirect if already logged in

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard_home')
        else:
            return render(request, 'dashboard/login.html', {'form': {}, 'error': 'Invalid credentials'})
    return render(request, 'dashboard/login.html', {'form': {}})

# Logout View
@login_required(login_url='dashboard_login')
def dashboard_logout(request):
    logout(request)
    return redirect('dashboard_login')

