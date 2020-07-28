from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField( max_length=50)
    prix = models.FloatField()
    quantity = models.FloatField()
    prixAchat = models.FloatField()
    margeBeneficiere = models.FloatField()
    TVA = models.FloatField()
    
    def __str__(self):
       return self.name
