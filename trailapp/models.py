from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=40)
    type = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    
class Testing(models.Model):
    name = models.CharField(max_length=40)
    status = models.BooleanField(default=False)
    
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='testing')