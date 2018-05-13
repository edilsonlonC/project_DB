from django.db import models

# Create your models here.
class Mark (models.Model):
    Serial=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=25)
    Country=models.CharField(max_length=25)

    def __str__ (self):
        return self.Name
