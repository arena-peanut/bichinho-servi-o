from django.contrib import admin
from .models import Animal, Specie, Status

admin.site.register(Animal)
admin.site.register(Status)
admin.site.register(Specie)
