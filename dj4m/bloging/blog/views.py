from django.shortcuts import render , redirect
from django.contrib import messages
from blog.models import Post, BlogComment
# Create your views here.
def blogHome(request):
	allposts=Post.objects.all()
	return render(request,'blog/blogHome.html',{'allPosts':allposts})

def blogPost(request, slug):
	post=Post.objects.filter(slug=slug).first()
	comments=BlogComment.objects.filter(post=post)
	context={'mypost':post,'comments':comments,'user':request.user}
	return render(request,'blog/blogPost.html',context)

def postComment(request):
	if request.method=='POST':
		comment = request.POST.get('comment')
		user = request.user
		postSno=request.POST.get('postSno')
		print(comment)
		print(postSno)
		post = Post.objects.get(sno=postSno)
		comment=BlogComment(comment=comment,user=user,post=post)
		comment.save()
		messages.success(request,"Your comment has been Uploaded")
	return redirect(f'/blog/{post.slug}')
