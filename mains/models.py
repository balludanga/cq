from django.db import models
from django.urls import reverse
# Create your models here.
class Mains(models.Model):
    title = models.CharField(max_length= 100)
    
    
    
    #view_count = models.ForeignKey(default=0)
    
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
        return reverse('mains-post', kwargs={
            'pk': self.pk
        })