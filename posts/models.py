import re
from django.db import models
import datetime

from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator
from model_utils.managers import InheritanceManager

from embed_video.fields import EmbedVideoField

User = get_user_model()















    

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField()
    about = models.TextField()

    def get_absolute_url(self):
        return reverse('author', kwargs={
            'pk': self.pk
        })

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=20)


    def get_absolute_url(self):
        return reverse('list_by_category', kwargs={
            'pk': self.pk
        })

    def __str__(self):
        return self.title

    

class Post(models.Model):
    title = models.CharField(max_length= 100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    time_to_read = models.IntegerField(default=0)
    #view_count = models.ForeignKey(default=0)
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    content = RichTextField()
    featured = models.BooleanField()
    
    video = EmbedVideoField()
    
    

    views = models.IntegerField(default=0)

    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    
    related_post = models.ForeignKey(
        'self', related_name='related', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'pk': self.pk
        })



class Logo(models.Model):
    logo_pic = models.ImageField()



