import os
import requests
import pickle
from io import BytesIO
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, ModelosPrediccion, Prediccion
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

@receiver(post_save, sender=User)
def crear_prediccion(sender, instance, created, **kwargs):
    if created:
        municipio = instance.municipio
        
        # Obtener el modelo entrenado desde la base de datos
        try:
            modelo_prediccion = ModelosPrediccion.objects.get(municipio=municipio)
            modelo = pickle.loads(modelo_prediccion.modeloblob)
        except ModelosPrediccion.DoesNotExist:
            print(f"No se encontró un modelo para el municipio {municipio}.")
            return
        
        # Obtener los datos de entrada desde la API
        url = "https://www.datos.gov.co/resource/sbwg-7ju4.json?$query=SELECT%20%60fechaobservacion%60%2C%20%60valorobservado%60%2C%20%60departamento%60%2C%20%60municipio%60%0AWHERE%20%60fechaobservacion%60%20%3E%20%222024-11-09T09%3A19%3A44%22%20%3A%3A%20floating_timestamp%0AORDER%20BY%20%60fechaobservacion%60%20DESC%20NULL%20LAST"
        response = requests.get(url)
        data = response.json()
        
        # Filtrar los datos para el municipio del usuario
        datos_municipio = [d for d in data if d['municipio'] == municipio]
        
        if len(datos_municipio) < 3:
            print(f"No hay suficientes datos para realizar la predicción para el municipio {municipio}.")
            return
        
        # Preparar los datos de entrada para la predicción
        X = []
        for i in range(3):
            fechaobservacion = datetime.strptime(datos_municipio[i]['fechaobservacion'], '%Y %b %d %I:%M:%S %p')
            valorobservado = float(datos_municipio[i]['valorobservado'])
            X.append([fechaobservacion.year, fechaobservacion.month, fechaobservacion.day, fechaobservacion.hour, valorobservado])
        
        # Realizar las predicciones para los próximos 3 días
        predicciones = modelo.predict(X)
        
        # Guardar las predicciones en la base de datos
        prediccion = Prediccion(
            valorpredicciontoday=predicciones[0],
            valorpredicciontomorrow=predicciones[1],
            valorprediccionaftertomorrow=predicciones[2],
            municipioprediccion=municipio,
            departamentoprediccion=datos_municipio[0]['departamento']
        )
        prediccion.save()
        print(f"Predicciones para {municipio} guardadas correctamente.")