import imp
from tkinter import CASCADE
from unicodedata import category
from django.db import models
from category.models import category
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    product_Id=models.IntegerField(unique=True)
    product_name=models.CharField(max_length=50, unique=True)
    slug        = models.SlugField(max_length=50, unique=True)
    description = models.CharField(max_length=500, blank=False)
    price       = models.IntegerField()
    del_price   = models.IntegerField(default=0)
    images      = models.ImageField(upload_to='photos/products',default=0)
    stock       = models.IntegerField()
    is_available = models.BooleanField(default=True)
    Category     = models.ForeignKey(category, on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_date=models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('product_detail',args=[self.Category.slug,self.slug])



    def __str__(self):
        return self.product_name