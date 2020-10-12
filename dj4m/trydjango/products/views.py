from django.shortcuts import render,get_object_or_404, redirect

# Create your views here.
from .models import Product
from .forms import ProductForm, RawProductFrom

#def product_create_view(request):
#	my_form=RawProductFrom()
#	if request.method == "POST":
#		my_form= RawProductFrom(request.POST)
#		if my_form.is_valid():
#			print(my_form.cleaned_data)
#			Product.objects.create(**my_form.cleaned_data)
#		else:
#			print(my_form.errors)
#	context={
#		'form':my_form
#	}
#	return render(request,'products/product_create.html',context)

def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
	context = {
        'form': form
	}
	return render(request, "products/product_create.html", context)

def product_update_view(request,id):
	obj=Product.objects.get(id=id)
	form=ProductForm(request.POST or None,instance=obj)
	if form.is_valid():
		form.save()
		
	context={
		"form":form
	}
	return render(request,'products/product_create.html',context)

def product_detail_view(request,id):
	obj=Product.objects.get(id=id)
	#context={
	#	"title": obj.title,
	#	"description" : obj.description,
	#	"price" : obj.price
	#}
	context={
		"object":obj
	}
	return render(request,'product/detail.html',context)

def product_delete_view(request, id):
	obj = get_object_or_404(Product, id=id)
	if request.method == "POST":
		obj.delete()
		return redirect('../../')
	context = {
        "object": obj
	}
	return render(request, "products/product_delete.html", context)

def product_list_view(request):
	queryset = Product.objects.all() # list of objects
	context = {
        "object_list": queryset
	}
	return render(request, "products/product_list.html", context)