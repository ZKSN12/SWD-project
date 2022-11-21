from django.db import models

# Create your models here.

class PetInfo(models.Model):
    info = models.CharField(max_length=120)
    pic = models.ImageField(null=True, blank=True, upload_to='images/')
    introduction = models.CharField(max_length=200)

    def __str__(self):
        return self.info

