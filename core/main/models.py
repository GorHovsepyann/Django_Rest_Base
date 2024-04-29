from django.db import models

# Create your models here.

class Category(models.Model):
    
    name = models.CharField('Car Category',max_length=250)
    def __str__(self) -> str:
        return self.name

class Car(models.Model):
    
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='cat_car',null=True)
    name = models.CharField('Car model',max_length=250)
    
    def __str__(self) -> str:
        return self.name
    
