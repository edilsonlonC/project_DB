from django.db import models
from apps.sales.models import Sale
from apps.mark.models import Mark

# Create your models here.
class Category (models.Model):
    Type=models.CharField(max_length=25)

    def __str__ (self):
        return self.Type

class Material (models.Model):
    Material=models.CharField(max_length=25)
    def __str__ (self):
        return self.Material

class Instruments (models.Model):
    ID=models.IntegerField(primary_key=True)
    Model=models.CharField(max_length=25)
    Quantity=models.IntegerField()
    Price=models.FloatField()
    Id_Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    Id_Material=models.ForeignKey(Material,on_delete=models.CASCADE)
    id_Sale=models.ForeignKey(Sale,null=True,blank=True,on_delete=models.CASCADE)
    id_Mark=models.ForeignKey(Mark,null=True,blank=True,on_delete=models.CASCADE)

    def __str__ (self):
        return self.Model
