from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'is_paid', 'is_delivered', 'updated_at', 'created_at')
    inlines = [OrderItemInline]