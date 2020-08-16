
from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
 
from clubFit.models import Informacion
from clubFit.models import Archivo

@admin.register(Informacion)

class InformacionAdmin(ImportExportModelAdmin):
	list_display=("codigoEstacion","nombreEstacion","latitud","longitud","altitud","categoria","entidad","areaOperativa","departamento","municipio","fechaInstalacion","fechaSuspension","idParametro","etiqueta", "descripcionSerie","frecuencia","fecha", "valor","grado", "calificador", "nivelAprovacion", "archivo")
	pass

@admin.register(Archivo)

class ArchivoAdmin(ImportExportModelArchivo):
	list_display=("fecha","nombre_archivo","nombre_interno","numero_registro","usuarios")
	pass


		


	
