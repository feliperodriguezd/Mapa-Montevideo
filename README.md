# Mapas Montevideo
## Funcionalidad:
Este proyecto muestra un mapa con las calles de Montevideo con los ómnibus en circulación en ese momento y sus respectivas paradas.

La información de las paradas y de los ómnibus es extraída de la API de la intendencia de Montevideo. 

Dada una parada especifica carga los próximos ómnibus en parar en esa parada. 

## Código

Se utilizan las librerías: request, http.client, json, matplotlib y geopandas.

El mapa de Montevideo esta dividió en 10 secciones para que la carga del mismo sea más aguil.

La carpeta Data contiene los archivos Json y Geojson con la información que no cambia (paradas y calles de Montevideo).

createGraph.py contiene las funciones que crean el grafico.

Exeptiones.py cuenta con las excepciones creadas. 

GetData.py contiene las funciones que utilizan la api de la intendencia para obtener la información de los ómnibus.

GetToken.py genera el token variable que requiere la api de la intendencia para acceder a ella, se usan las librerías http.client y json.

Main.py ejecuta el código principal.

AuxiliaryFunctions.py tiene funciones auxiliares utilizadas.

Proyecto en construcción.