from rest_framework import viewsets
from .models import Parking
from .serializers import ParkingSerializer

class ParkingViewSet(viewsets.ModelViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer

