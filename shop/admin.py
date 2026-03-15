"""
Admin configuration with enhanced product management.
"""

from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Category, Product, ProductReview, Cart, CartItem,
    Order, OrderItem, Wishlist, WishlistItem
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin."""
    list_display = ['name', 'slug', 'get_product_count', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product admin with pricing display."""
    list_display = ['name', 'category', 'get_price_display', 'stock', 'get_rating', 'is_featured', 'is_active']
    list_filter = ['category', 'is_active', 'is_featured', 'created_at']
    search_fields = ['name', 'sku']
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Basic Info', {'fields': ('name', 'slug', 'description', 'category', 'sku')}),
        ('Pricing', {'fields': ('price', 'discount_price')}),
        ('Media', {'fields': ('image', 'image_alt', 'image_alt2')}),
        ('Stock & Status', {'fields': ('stock', 'is_active', 'is_featured')}),
    )

    def get_price_display(self, obj):
        if obj.discount_price:
            return format_html(
                '<span style="text-decoration: line-through;">${}</span> → <span style="color: green;">${}</span>',
                obj.price, obj.discount_price
            )
        return f"${obj.price}"
    get_price_display.short_description = 'Price'

    def get_rating(self, obj):
        rating = obj.get_average_rating()
        return f"{'⭐' * int(rating)} {rating}/5" if rating else "No reviews"
    get_rating.short_description = 'Rating'


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    """Product review admin."""
    list_display = ['product', 'user', 'get_rating_stars', 'is_approved', 'created_at']
    list_filter = ['is_approved', 'rating', 'created_at']
    search_fields = ['product__name', 'user__username']
    readonly_fields = ['created_at', 'updated_at']
    actions = ['approve_reviews', 'disapprove_reviews']

    def get_rating_stars(self, obj):
        return f"{'⭐' * obj.rating}"
    get_rating_stars.short_description = 'Rating'

    def approve_reviews(self, request, queryset):
        queryset.update(is_approved=True)

    def disapprove_reviews(self, request, queryset):
        queryset.update(is_approved=False)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Order admin with status badge."""
    list_display = ['order_number', 'user', 'get_total', 'get_status_badge', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['order_number', 'user__username', 'email']
    readonly_fields = ['order_number', 'created_at']
    fieldsets = (
        ('Order', {'fields': ('order_number', 'user', 'total_amount', 'status', 'tracking_number')}),
        ('Customer', {'fields': ('full_name', 'email', 'phone')}),
        ('Address', {'fields': ('address', 'city', 'postal_code')}),
    )
    inlines = []

    def get_total(self, obj):
        return f"${obj.total_amount}"
    get_total.short_description = 'Total'

    def get_status_badge(self, obj):
        colors = {
            'pending': '#ff9800', 'processing': '#2196F3',
            'shipped': '#9C27B0', 'delivered': '#4CAF50', 'cancelled': '#f44336'
        }
        return format_html(
            '<span style="background-color: {}; color: white; padding: 5px 10px; border-radius: 3px;">{}</span>',
            colors.get(obj.status), obj.get_status_display()
        )
    get_status_badge.short_description = 'Status'


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    """Wishlist admin."""
    list_display = ['user', 'get_total_items', 'created_at']
    search_fields = ['user__username']

    def get_total_items(self, obj):
        return obj.get_total_items()
    get_total_items.short_description = 'Items'


admin.site.register(CartItem)
admin.site.register(WishlistItem)