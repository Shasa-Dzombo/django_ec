from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	"""Admin for Category model."""
	list_display = ("name", "description")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	"""Admin for Product model."""
	list_display = ("name", "price", "category", "stock")
	list_filter = ("category",)




