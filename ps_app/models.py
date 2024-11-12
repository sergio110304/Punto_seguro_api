from django.db import models
from .utils import obtener_latitud_longitud
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Users(models.Model):
    iduser = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.TextField(max_length=50)
    municipality = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Usuario {self.iduser}: {self.name} {self.lastname}"
    

class Stations(models.Model):
    codigoestacion = models.CharField(max_length=100, primary_key=True)
    nombreestacion = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    zonahidrografica = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()
    
    def __str__(self):
        return f"Estación {self.codigoestacion}: {self.nombreestacion}"

class Sensors(models.Model):
    codigosensor = models.CharField(max_length=50, primary_key=True)
    descripcionsensor = models.CharField(max_length=50)
    unidadmedida = models.CharField(max_length=20)

    def __str__(self):
        return f"Sensor {self.codigosensor}: {self.descripcionsensor}"  
    
    
class Observations(models.Model):
    idobservacion = models.AutoField(primary_key=True)
    codigoestacion = models.CharField(max_length=100)
    codigosensor = models.CharField(max_length=100)
    fechaobservacion = models.DateTimeField()
    valorobservado = models.FloatField()
    
    def __str__(self):
        return f"Observación {self.idobservacion}, Fecha {self.fechaobservacion}"  
    

class UserLocation(models.Model):
    userid = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    direccioncasa = models.TextField(max_length=50)
    latitudcasa = models.FloatField()
    longitudcasa = models.FloatField()
    ubicacionactual = models.CharField(max_length=100)
    latitudactual = models.FloatField()
    longitudactual = models.FloatField()

    def __str__(self):
        return f"Ubicación de {self.userid}: casa: {self.direccioncasa} --- actual: {self.ubicacionactual}"

                                     
class MeetingPoint(models.Model):
    nombreSede = models.CharField(max_length=200)
    departamentoSedeDesc = models.CharField(max_length=150)
    municipioSedeDesc = models.CharField(max_length=150)
    emailSede = models.EmailField(max_length=200)
    telefonoSede = models.CharField(max_length=100)
    direccionSede = models.TextField(max_length=200)

    def __str__(self):
        return f"Punto de Encuentro: {self.nombreSede} en {self.departamentoSedeDesc}"
    
class ModelosPrediccion(models.Model):
    idmodelo = models.AutoField(primary_key=True)
    modeloblob = models.BinaryField()
    descripcion = models.TextField(max_length=100)
    municipio = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Modelo {self.idmodelo}: {self.descripcion}"
    
class ModelosPrediccionPrecipitacion(models.Model):
    idmodelo = models.AutoField(primary_key=True)
    modeloblob = models.BinaryField()
    descripcion = models.TextField(max_length=100)
    municipio = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Modelo {self.idmodelo}: {self.descripcion}"

@receiver(post_save, sender=Users)
def actualizar_ubicacion_usuario(sender, instance, **kwargs):
    latitud, longitud = obtener_latitud_longitud(instance.department, instance.municipality, instance.address)
    if latitud and longitud:
        UserLocation.objects.update_or_create(
            userid=instance,
            defaults={
                'direccioncasa': instance.address,
                'latitudcasa': latitud,
                'longitudcasa': longitud,
                'ubicacionactual': f"{latitud}, {longitud}",
                'latitudactual': latitud,
                'longitudactual': longitud
            }
        )