"""
Views for improved e-commerce application.
Includes: Products, Reviews, Wishlist, Cart, Orders with Pagination
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import uuid

from .models import (
    Product, Category, Cart, CartItem, Order, OrderItem,
    ProductReview, Wishlist, WishlistItem
)
from .forms import (
    UserRegistrationForm, LoginForm, CheckoutForm, ProductReviewForm
)


# ===================== AUTHENTICATION =====================

def register(request):
    """User registration view."""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Cart.objects.create(user=user)
            Wishlist.objects.create(user=user)
            messages.success(request, 'Account created! Please login.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    """User login view."""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def user_logout(request):
    """User logout view."""
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('login')


# ===================== PRODUCTS =====================

def home(request):
    """Home page with featured and paginated products."""
    products = Product.objects.filter(is_active=True).select_related('category')
    categories = Category.objects.filter(is_active=True)
    query = request.GET.get('q')
    category_id = request.GET.get('category')
    sort = request.GET.get('sort', '-created_at')

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    if category_id:
        products = products.filter(category_id=category_id)

    if sort in ['price', '-price', '-created_at', 'name']:
        products = products.order_by(sort)

    # Pagination
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    featured_products = Product.objects.filter(is_active=True, is_featured=True)[:6]

    context = {
        'products': products,
        'categories': categories,
        'featured_products': featured_products,
        'query': query,
        'category_id': category_id,
        'sort': sort,
    }
    return render(request, 'home.html', context)


def category_detail(request, slug):
    """Category detail page with products."""
    category = get_object_or_404(Category, slug=slug, is_active=True)
    products = Product.objects.filter(category=category, is_active=True)
    
    query = request.GET.get('q')
    sort = request.GET.get('sort', '-created_at')

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    if sort in ['price', '-price', '-created_at', 'name']:
        products = products.order_by(sort)

    # Pagination
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    categories = Category.objects.filter(is_active=True)

    context = {
        'category': category,
        'products': products,
        'categories': categories,
        'query': query,
        'sort': sort,
    }
    return render(request, 'category_detail.html', context)


def product_detail(request, slug):
    """Product detail with reviews and wishlist."""
    product = get_object_or_404(Product, slug=slug, is_active=True)
    reviews = product.reviews.filter(is_approved=True).order_by('-created_at')
    related_products = Product.objects.filter(category=product.category, is_active=True).exclude(id=product.id)[:4]
    
    in_wishlist = False
    if request.user.is_authenticated:
        in_wishlist = WishlistItem.objects.filter(
            wishlist__user=request.user,
            product=product
        ).exists()

    # Review pagination
    paginator = Paginator(reviews, 5)
    page = request.GET.get('page')
    
    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)

    review_form = ProductReviewForm()
    user_review = None
    
    if request.user.is_authenticated:
        user_review = ProductReview.objects.filter(product=product, user=request.user).first()

    context = {
        'product': product,
        'reviews': reviews,
        'user_review': user_review,
        'review_form': review_form,
        'related_products': related_products,
        'in_wishlist': in_wishlist,
        'average_rating': product.get_average_rating(),
        'review_count': product.get_review_count(),
    }
    return render(request, 'product_detail.html', context)


# ===================== REVIEWS =====================

@login_required(login_url='login')
@require_POST
def add_review(request, product_id):
    """Add/update product review."""
    product = get_object_or_404(Product, id=product_id)
    form = ProductReviewForm(request.POST)
    
    if form.is_valid():
        review, created = ProductReview.objects.update_or_create(
            product=product,
            user=request.user,
            defaults={
                'title': form.cleaned_data['title'],
                'content': form.cleaned_data['content'],
                'rating': form.cleaned_data['rating'],
            }
        )
        
        msg = 'Review submitted!' if created else 'Review updated!'
        messages.success(request, msg)
    else:
        messages.error(request, 'Error submitting review.')

    return redirect('product_detail', slug=product.slug)


# ===================== WISHLIST =====================

def get_or_create_wishlist(user):
    """Get or create user wishlist."""
    wishlist, _ = Wishlist.objects.get_or_create(user=user)
    return wishlist


@login_required(login_url='login')
@require_POST
def add_to_wishlist(request, product_id):
    """Add product to wishlist."""
    product = get_object_or_404(Product, id=product_id)
    wishlist = get_or_create_wishlist(request.user)
    
    wishlist_item, created = WishlistItem.objects.get_or_create(
        wishlist=wishlist,
        product=product
    )
    
    if created:
        messages.success(request, f'{product.name} added to wishlist!')
    else:
        messages.info(request, 'Already in wishlist.')
    
    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required(login_url='login')
@require_POST
def remove_from_wishlist(request, item_id):
    """Remove product from wishlist."""
    wishlist_item = get_object_or_404(
        WishlistItem,
        id=item_id,
        wishlist__user=request.user
    )
    product_name = wishlist_item.product.name
    wishlist_item.delete()
    messages.success(request, f'{product_name} removed from wishlist.')
    
    return redirect(request.META.get('HTTP_REFERER', 'wishlist'))


@login_required(login_url='login')
def wishlist_view(request):
    """Display user's wishlist."""
    wishlist = get_or_create_wishlist(request.user)
    wishlist_items = wishlist.items.all().select_related('product')

    paginator = Paginator(wishlist_items, 12)
    page = request.GET.get('page')
    
    try:
        wishlist_items = paginator.page(page)
    except PageNotAnInteger:
        wishlist_items = paginator.page(1)
    except EmptyPage:
        wishlist_items = paginator.page(paginator.num_pages)

    context = {
        'wishlist': wishlist,
        'wishlist_items': wishlist_items,
    }
    return render(request, 'wishlist.html', context)


# ===================== CART =====================

def get_or_create_cart(user):
    """Get or create user cart."""
    cart, _ = Cart.objects.get_or_create(user=user)
    return cart


@login_required(login_url='login')
@require_POST
def add_to_cart(request, product_id):
    """Add product to cart."""
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))

    if quantity <= 0:
        messages.error(request, 'Invalid quantity.')
        return redirect('product_detail', slug=product.slug)

    if not product.is_in_stock():
        messages.error(request, 'Out of stock.')
        return redirect('product_detail', slug=product.slug)

    if product.stock < quantity:
        messages.error(request, f'Only {product.stock} available.')
        return redirect('product_detail', slug=product.slug)

    cart = get_or_create_cart(request.user)
    
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': quantity}
    )

    if not created:
        cart_item.quantity += quantity
        cart_item.save()

    messages.success(request, f'{product.name} added to cart!')
    return redirect('cart')


@login_required(login_url='login')
def cart_view(request):
    """Display shopping cart."""
    cart = get_or_create_cart(request.user)
    cart_items = cart.cartitem_set.all().select_related('product')

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': cart.get_total_price(),
        'total_items': cart.get_total_items(),
    }
    return render(request, 'cart.html', context)


@login_required(login_url='login')
@require_POST
def update_cart_item(request, item_id):
    """Update cart item quantity."""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    quantity = int(request.POST.get('quantity', 1))

    if quantity <= 0:
        cart_item.delete()
        messages.success(request, 'Item removed.')
    else:
        if cart_item.product.stock < quantity:
            messages.error(request, 'Insufficient stock.')
        else:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, 'Cart updated.')

    return redirect('cart')


@login_required(login_url='login')
@require_POST
def remove_from_cart(request, item_id):
    """Remove item from cart."""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    product_name = cart_item.product.name
    cart_item.delete()
    messages.success(request, f'{product_name} removed.')
    return redirect('cart')


# ===================== ORDERS =====================

@login_required(login_url='login')
def checkout(request):
    """Checkout page."""
    cart = get_or_create_cart(request.user)
    cart_items = cart.cartitem_set.all()

    if not cart_items.exists():
        messages.error(request, 'Cart is empty!')
        return redirect('cart')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order_number = f"ORD-{uuid.uuid4().hex[:8].upper()}"

            order = Order.objects.create(
                user=request.user,
                order_number=order_number,
                total_amount=cart.get_total_price(),
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                postal_code=form.cleaned_data['postal_code'],
            )

            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.get_display_price(),
                )

            cart_items.delete()
            messages.success(request, 'Order placed!')
            return redirect('order_confirmation', order_id=order.id)
    else:
        form = CheckoutForm(initial={
            'full_name': f"{request.user.first_name} {request.user.last_name}".strip(),
            'email': request.user.email,
        })

    context = {
        'form': form,
        'cart': cart,
        'cart_items': cart_items,
    }
    return render(request, 'checkout.html', context)


@login_required(login_url='login')
def order_confirmation(request, order_id):
    """Order confirmation page."""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order_items = order.items.all()

    context = {
        'order': order,
        'order_items': order_items,
    }
    return render(request, 'order_confirmation.html', context)


@login_required(login_url='login')
def order_history(request):
    """User order history with pagination."""
    orders = Order.objects.filter(user=request.user).prefetch_related('items')

    paginator = Paginator(orders, 10)
    page = request.GET.get('page')
    
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    context = {'orders': orders}
    return render(request, 'order_history.html', context)