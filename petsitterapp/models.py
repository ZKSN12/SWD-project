from django.db import models

# Create your models here.


class SitterProfile(models.Model):
    name = models.CharField(max_length=120)
    url = models.URLField(max_length=200, default='petsitterapp/jason/')
    sitter_img = models.ImageField(null=True, upload_to='images/')
    address = models.CharField(max_length=120)
    introduction = models.CharField(max_length=200)
    story = models.TextField(null=True, max_length=5000)
    price = models.CharField(max_length=120)
    price_number = models.IntegerField(null=True)
    zipcode = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.CharField(max_length=120)
    comment = models.TextField(max_length=2000)
    sitterProfile = models.ForeignKey(SitterProfile, related_name="comments",blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.sitterProfile.name


