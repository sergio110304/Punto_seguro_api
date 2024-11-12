# Punto Seguro API

**Tema**: Ambiente y Desarrollo Sostenible  
**Convocatoria**: “Datos a la U”  
**Universidad del Norte**  
**Ingeniería de Sistemas**

## Descripción

La API de **Punto Seguro** es una API RESTful que permite a las aplicaciones consumir datos climáticos, geográficos y de seguridad pública para mejorar la preparación y respuesta ante emergencias climáticas en Colombia. Proporciona información sobre el clima, puntos de emergencia cercanos y consejos prácticos para actuar durante emergencias. Está diseñada para ser integrada con aplicaciones móviles y web.

## Instalación

Para instalar y ejecutar la API en tu entorno local, sigue estos pasos:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/sergio110304/Punto_seguro_api.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd Punto_seguro_api
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta la API:
   ```bash
   python manage.py runserver
   ```

La API estará disponible en `http://127.0.0.1:8000`.

## Referencias
- [Datos Abiertos, "Registro Especial de Prestadores y Sedes de Servicios de Salud", Datos.gov.co, 2024.](https://www.datos.gov.co)
- [Datos Abiertos, "Precipitación", Datos.gov.co, 2024.](https://www.datos.gov.co)
- [Datos Abiertos, "Presión Atmosférica", Datos.gov.co, 2024.](https://www.datos.gov.co)
- [Datos Abiertos, "Dirección Viento", Datos.gov.co, 2024.](https://www.datos.gov.co)
- [Datos Abiertos, "Humedad del Aire 2 metros", Datos.gov.co, 2024.](https://www.datos.gov.co)
- [Datos Abiertos, "Datos Hidrometeorológicos Crudos - Red de Estaciones IDEAM : Temperatura", Datos.gov.co, 2024.](https://www.datos.gov.co)
- [Defensa Civil Colombiana, “Recomendaciones - Defensa Civil Colombiana,” Defensacivil.gov.co, 2022.](https://www.defensacivil.gov.co)
