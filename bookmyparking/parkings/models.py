from django.db import models

class Parking(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()

    def __str__(self):
        return self.nom

