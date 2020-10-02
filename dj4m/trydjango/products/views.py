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
	obj=Product.objects.get(id=1)
	form=ProductForm(request.POST or None,instance=obj)
	if form.is_valid():
		form.save()
		
	context={
		"form":form
	}
	return render(request,'products/product_create.html',context)

def product_detail_view(request,my_id):
	obj=Product.objects.get(id=my_id)
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