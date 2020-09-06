from django.shortcuts import render , redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
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

def search(request):
	query=request.GET['query']
	#allposts=Post.objects.all()
	if len(query)>78:
		allposts=Post.objects.none()
	else:
		allpost=Post.objects.filter(title__icontains=query)
		allpostcontent=Post.objects.filter(content__icontains=query)
		allposts=allpost.union(allpostcontent)
	if allposts.count()!= 0:
		messages.success(request, 'Found')
	contents={'allPosts':allposts,'query':query}
	return render(request,"home/search.html",contents)

def handleSignup(request):
	if request.method=='POST':
		username=request.POST['username']
		firstname=request.POST['fname']
		lastname=request.POST['lname']
		email=request.POST['email']
		pass1=request.POST['pass1']
		pass2=request.POST['pass2']
		myuser=User.objects.create_user(username,email,pass1)
		myuser.first_name=firstname
		myuser.last_name=lastname
		myuser.save()
		messages.success(request,"Your account has been created successfully.")
		return redirect('/')
	else:
		messages.error(request,"Please fill the form carefully.")
		return redirect('/')
