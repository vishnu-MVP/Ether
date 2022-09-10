from distutils.command.upload import upload
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class category(models.Model):
    category_name=models.CharField(max_length=50)
    slug = models.CharField(max_length=100,unique=True)
    description= models.TextField(max_length=255,blank=False)
    cat_img= models.ImageField(upload_to='photos/categories',blank=False)

    class meta :
        verbose_name ='category'
        verbose_name_plural ='categories'
    
    def __str__(self):
        return self.category_name