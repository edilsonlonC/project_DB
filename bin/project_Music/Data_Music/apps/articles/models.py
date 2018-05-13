from django.db import models
from apps.instruments.models import Material

# Create your models here.

class Article (models.Model):
    Description=models.CharField(max_length=25)
    precio=models.FloatField()
    Id_Material=models.ForeignKey(Material,on_delete=models.CASCADE,null=True)
