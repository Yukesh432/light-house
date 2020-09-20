from django.contrib import admin

from .models import Category, Product, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price', 'is_published', 'is_topselling')
    list_editable = ('is_published', 'is_topselling',)
    list_display_link = ('id', 'title')
    search_fields = ('name', 'email')
    list_per_page = 20

admin.site.register(Product, ProductAdmin)

class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_editable = ('slug',)
    list_display_link = ('name')
    search_fields = ('name', 'email')
    list_per_page = 20
admin.site.register(Category, CatAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'name', 'address', 'email', 'items_json')
   
    list_display_link = ('name')
    search_fields = ('name', 'email')
    list_per_page = 20
admin.site.register(Order, OrderAdmin)

