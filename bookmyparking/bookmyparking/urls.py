from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from parkings.views import ParkingViewSet
from places.views import PlaceViewSet, ReservationViewSet

# Création d'un routeur et enregistrement de nos viewsets
router = DefaultRouter()
router.register(r'parkings', ParkingViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'reservations', ReservationViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

