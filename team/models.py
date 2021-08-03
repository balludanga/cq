from django.db import models
from django.urls import reverse
# Create your models here.

class Team_member(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="team_member/")
    about = models.TextField(max_length=255)

    def get_absolute_url(self):
        return reverse('team-member', kwargs={
            'pk': self.pk
        })
