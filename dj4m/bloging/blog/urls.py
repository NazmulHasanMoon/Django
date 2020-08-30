from django.urls import path , include
from . import views
urlpatterns = [
    	path('', views.blogHome, name='blogHome'),
	path('blogpost/',views.blogPost,name='blogPost'),
]
