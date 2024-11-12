from rest_framework import serializers
from .models import Users, Observations, Stations, Sensors, UserLocation, MeetingPoint, ModelosPrediccion, Prediccion

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        read_only_fields = ['iduser']

class ObservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observations
        fields = '__all__'
        read_only_fields = ['idobservacion']

class StationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stations
        fields = '__all__'

class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensors
        fields = '__all__'

class UserLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLocation
        fields = '__all__'
        read_only_fields = ['userid']

class MeetingPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingPoint
        fields = '__all__'

class ModelosPrediccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelosPrediccion
        fields = '__all__'
        
class PrediccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediccion
        fields = '__all__'