from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product
from .products import CategoryForm, ProductForm


def home(request):
	form =CategoryForm()
	return render(request, "home.html", {"form": form}) 

def add_product(request):
	if request.method== "POST":
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			#pass message
			return redirect("products:add_product")
	else:
		form =ProductForm()
	return render(request,"products/product_form.html", {"form": form})

def get_all(request):
	category= Category.objects.all()
	return render(request, "products/category_list.html",{'category':category})
    