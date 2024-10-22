from django.db import models

# Create your models here.
class Blogs(models.Model):
    img = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title