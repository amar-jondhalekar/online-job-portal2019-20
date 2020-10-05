from django.db import models
from django.contrib.auth.models import User
from django import forms


class JobPosts(models.Model):
   job_title=models.CharField(max_length=100)
   salary=models.CharField(max_length = 20, blank=True, default=None)
   company=models.CharField(max_length=100)
   job_type=models.CharField(max_length = 20, blank=True, default=None)
   location=models.CharField(max_length=100)
   description=models.CharField(max_length=300)
   image=models.ImageField(upload_to='jobposts')
   created_on=models.DateTimeField(auto_now_add=True)


class Resume(models.Model):
   resume=models.FileField(upload_to='documents')
   user= models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='resume')