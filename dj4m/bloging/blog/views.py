from django.shortcuts import render
from django.contrib import messages
from blog.models import Post
# Create your views here.
def blogHome(request):
	allposts=Post.objects.all()
	return render(request,'blog/blogHome.html',{'allPosts':allposts})

def blogPost(request, slug):
	return render(request,'blog/blogPost.html')
