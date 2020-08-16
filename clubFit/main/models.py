from django.db import models

# Create your models here.



class Usuarios (models.Model):

	nombres = models.CharField(max_length=45)
	apellidos = models.CharField(max_length=45)
	correo = models.CharField(max_length=45)

	usuario = models.CharField(max_length=30)
	contrasena = models.CharField(max_length=255)

	class Meta:
		db_table = 'usuarios'


class Archivo (models.Model):
		
	fecha = models.DateField(blank=True, null=True)
	nombre_archivo = models.CharField(max_length=255)
	nombre_interno = models.CharField(max_length=255)
	numero_registro =models.IntegerField()
	
	usuarios = models.ForeignKey(Usuarios, models.DO_NOTHING)

	class Meta:
		db_table = 'archivo'

class Informacion (models.Model):
	
	#tabla orden trabajo
	
	codigoEstacion = models.CharField(max_length=45)
	nombreEstacion = models.CharField(max_length=45)
	latitud = models.CharField(max_length=45)
	longitud = models.CharField(max_length=45)
	altitud = models.CharField(max_length=45)
	categoria = models.CharField(max_length=45)
	entidad = models.CharField(max_length=45)
	areaOperativa = models.CharField(max_length=45)
	departamento = models.CharField(max_length=45)
	municipio  = models.CharField(max_length=45)
	fechaInstalacion = models.DateField(blank=True, null=True)
	fechaSuspension = models.DateField(blank=True, null=True)
	idParametro = models.CharField(max_length=45)
	etiqueta = models.CharField(max_length=45)
	descripcionSerie = models.CharField(max_length=45)
	frecuencia = models.CharField(max_length=45)
	fecha = models.DateField(blank=True, null=True)
 
	valor = models.DecimalField(max_digits=5, decimal_places=2)
	grado = models.CharField(max_length=45)
	calificador = models.CharField(max_length=45)
	nivelAprovacion = models.CharField(max_length=45)
  
	archivo = models.ForeignKey(Archivo, models.DO_NOTHING)
	
	class Meta:
		db_table = 'informacion'

