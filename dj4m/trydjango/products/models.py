from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
	title		= models.CharField(max_length=50) #max_length=required
	description	= models.TextField(blank=True, null=True)
	price		= models.DecimalField(max_digits=1000, decimal_places=2)
	summary		= models.TextField(blank=False, null=False)
	featured	= models.BooleanField(default=False)  # null=True or default=True

	def get_absolute_url(self):
		return reverse("products:product-detail",kwargs={"id":self.id})#f"/product/{self.id}/"