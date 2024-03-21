from django.db import models

from django.db import models
from django.utils import timezone
from parkings.models import Parking

class TypePlace(models.TextChoices):
    MOTO = 'M', 'Moto'
    VOITURE = 'V', 'Voiture'
    HANDICAPE = 'H', 'Handicapé'

class Place(models.Model):
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE, related_name='places')
    type_place = models.CharField(max_length=1, choices=TypePlace.choices, default=TypePlace.VOITURE)
    numero = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.get_type_place_display()} - {self.numero} ({self.parking.nom})"

class Reservation(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='reservations')
    debut = models.DateTimeField()
    fin = models.DateTimeField()

    def is_active(self):
        now = timezone.now()
        return now >= self.debut and now <= self.fin

    def __str__(self):
        return f"Réservation {self.id} pour {self.place}"
