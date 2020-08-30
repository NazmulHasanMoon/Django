from django.shortcuts import render
from home.models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
	messages.info(request, 'Welcome to Home Page!')
	return render(request,"home/home.html")

def about(request):
	messages.info(request, 'Welcome to About Us Page!')
	return render(request,"home/about.html")

def contact(request):
	messages.info(request, 'Welcome to Contact Page!')
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		phone=request.POST['phone']
		content=request.POST['content']
		contact=Contact(name=name,email=email,phone=phone,content=content)
		contact.save()
	return render(request,"home/contact.html")
