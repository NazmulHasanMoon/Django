from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
class Post(models.Model):
	sno=models.AutoField(primary_key=True)
	title=models.CharField(max_length=250,blank=False)
	content=models.TextField()
	author= models.CharField(max_length=50, blank=False)
	slug = models.CharField(max_length=250,blank=False)	
	timeStamp=models.DateTimeField(auto_now=False, auto_now_add=True,blank=False)

	def __str__(self):
		return self.title + " by " + self.author
	
