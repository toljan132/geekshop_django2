from django.contrib import admin
from .models import ProductCategory, Product

# admin.site.register(ProductCategory)
# admin.site.register(Product)


class ProductInline(admin.TabularInline):
    model = Product
    fields = 'name', 'short_desc'
    extra = 1


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    inlines = ProductInline,


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = 'name', 'category__name',
    list_display = 'name', 'category', 'quantity', 'price',
    readonly_fields = 'price',