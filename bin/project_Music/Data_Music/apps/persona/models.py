from django.db import models

# Create your models here.

# una clase es una tabla
# un atributo de la clase es un campo en la tabla

class User (models.Model):
    Id = models.CharField(primary_key=True,max_length=50)
    Name =  models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Born_Date = models.DateField()
    admission_Date= models.DateField()
    power = models.BooleanField(default=False)
    salary = models.FloatField()
    Email = models.EmailField()

    def __str__ (self):
        return "%s %s"%(self.Name,self.LastName)
