from django.shortcuts import render
from django.contrib import messages
# Create your views here.
def blogHome(request):
	return render(request,'blog/blogHome.html')

def blogPost(request):
	return render(request,'blog/blogPost.html')
