from django.db import models

# Create your models here.

class Reviews(models.Model):
    name = models.CharField(max_length=120)
    content = models.TextField(max_length=2000)
    review_id = models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.name

class SitterProfile(models.Model):
    name = models.CharField(max_length=120)
    url = models.URLField(max_length=200, default='petsitterapp/jason/')
    sitter_img = models.ImageField(null=True, upload_to='images/')
    address = models.CharField(max_length=120)
    introduction = models.CharField(max_length=200)
    story = models.TextField(null=True, max_length=5000)
    price = models.CharField(max_length=120)

    def __str__(self):
        return self.name


