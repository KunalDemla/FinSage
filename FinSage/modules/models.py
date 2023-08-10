from django.db import models
from django.contrib.auth.models import User
from distutils.command.upload import upload
from PIL import Image

# Create your models here.
class Modules(models.Model):
    moduleId = models.CharField(max_length=250)
    title = models.CharField(max_length=250,blank=True)
    likes = models.ManyToManyField(User,related_name='favourite',default=None,blank=True)
    likeCount = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    image=models.ImageField(default='default.jpeg',upload_to='module_images')
    
    def __str__(self):
        return f'{self.title} Module'
    
    def save(self,*args,**kwargs):
        super(Modules,self).save(*args,**kwargs)

        img=Image.open(self.image.path)

        if img.height > 300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
