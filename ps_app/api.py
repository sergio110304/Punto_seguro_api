from .models import Users, Observations, Stations, Sensors, UserLocation
from rest_framework import viewsets, permissions
from .serializers import UsersSerializer, ObservationsSerializer, StationsSerializer, SensorsSerializer, UserLocationSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UsersSerializer


class ObservationsViewSet(viewsets.ModelViewSet):
    queryset = Observations.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ObservationsSerializer


class StationsViewSet(viewsets.ModelViewSet):
    queryset = Stations.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StationsSerializer


class SensorsViewSet(viewsets.ModelViewSet):
    queryset = Sensors.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SensorsSerializer

class UserLocationViewSet(viewsets.ModelViewSet):
    queryset = UserLocation.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserLocationSerializer