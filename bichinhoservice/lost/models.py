from django.db import models


class Status(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status


class Specie(models.Model):
    specie = models.CharField(max_length=50)

    def __str__(self):
        return self.specie


class Animal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.ForeignKey(Status, on_delete="cascade")
    specie = models.ForeignKey(Specie, on_delete="cascade")

    def __str__(self):
        return self.name
