import googlemaps
from django.conf import settings

def obtener_latitud_longitud(departamento, municipio, direccion):
    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
    direccion_completa = f"{direccion}, {municipio}, {departamento}, Colombia"
    geocode_result = gmaps.geocode(direccion_completa)
    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        return location['lat'], location['lng']
    return None, None

#print(obtener_latitud_longitud("Atlantico", "Barranquilla", "Calle 55 # 32"))