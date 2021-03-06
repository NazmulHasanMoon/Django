from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
class Contact(models.Model):
	sno=models.AutoField(primary_key=True)
	name=models.CharField(max_length=250,blank=False)
	phone=models.CharField(max_length=11,blank=False)
	email=models.CharField(max_length=50,blank=False)
	content=models.TextField()
	timeStamp=models.DateTimeField(auto_now=False, auto_now_add=True,blank=False)

	def __str__(self):
		return self.name
	
