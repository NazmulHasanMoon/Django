from django.shortcuts import render , redirect
from django.contrib import messages
from blog.models import Post, BlogComment
from blog.templatetags import task
# Create your views here.
def blogHome(request):
	allposts=Post.objects.all()
	return render(request,'blog/blogHome.html',{'allPosts':allposts})

def blogPost(request, slug):
	post=Post.objects.filter(slug=slug).first()
	comments=BlogComment.objects.filter(post=post,parent=None)
	replies=BlogComment.objects.filter(post=post).exclude(parent=None)
	repdic={}
	for reply in replies:
		if reply.sno not in repdic.keys():
			repdic[reply.parent.sno] = [reply]
		else:
			repdic[reply.parent.sno].append(reply)
	print(repdic)
	context={'mypost':post,'comments':comments,'user':request.user, 'replyDict':repdic}
	return render(request,'blog/blogPost.html',context)

def postComment(request):
	if request.method=='POST':
		comment = request.POST.get('comment')
		user = request.user
		postSno=request.POST.get('postSno')
		post = Post.objects.get(sno=postSno)
		parentSno = request.POST.get("parentSno")
		if parentSno=="":		
			comment = BlogComment(comment=comment,user=user,post=post)
			comment.save()
			messages.success(request,"Your Comment has been Uploaded")
		else:
			prnt = BlogComment.objects.get(sno=parentSno)
			comment = BlogComment(comment=comment,user=user,post=post,parent=prnt)
			comment.save()
			messages.success(request,"Your Reply has been Uploaded")
	return redirect(f'/blog/{post.slug}')
