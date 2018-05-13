from django.db import models
from apps.persona.models import User
# Create your models here.


class Sale (models.Model):
    Description=models.TextField(max_length=50)
    Id_user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    Date_sale=models.DateField(null=True)

    def __str__ (self):
        return self.Description
