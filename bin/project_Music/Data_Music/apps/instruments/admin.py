from django.contrib import admin
from apps.instruments.models import Category , Material , Instruments

# Register your models here.
admin.site.register(Category)
admin.site.register(Material)
admin.site.register(Instruments)
