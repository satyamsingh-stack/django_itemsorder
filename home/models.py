from django.db import models

# Create your models here.
class items(models.Model):
    item_id = models.AutoField(primary_key=True)  
    item_name = models.CharField(max_length=100)
    item_price = models.IntegerField()
    item_description = models.TextField()
    barcode=models.CharField(unique=True,max_length=255)
