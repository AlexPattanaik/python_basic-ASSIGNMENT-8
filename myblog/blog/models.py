from django.db import models

# Create your models here.
class blog(models.Model):
    def __str__(self):
        return self.blog_name

    blog_name=models.CharField(max_length=100)
    blog_info=models.CharField(max_length=500)
    blog_detail=models.CharField()
    blog_pic=models.ImageField(upload_to='blog_images/',default='default.img')

