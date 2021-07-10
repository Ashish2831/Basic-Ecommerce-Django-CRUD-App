from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_id', 'size']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'description', 'category_id']


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_id']


@admin.register(ProductImage)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_id', 'image']