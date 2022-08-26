from django.db import models

# Create your models here.


class UserProfile(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='profile_image')
    video = models.FileField(upload_to='videos')

    def __str__(self):
        return self.name
