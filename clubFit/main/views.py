from django.shortcuts import render
from django.http import HttpResponse

from .models import Usuarios
from .models import Archivo
from .models import Informacion

from django.shortcuts import redirect

##################################################

from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from datetime import timedelta, datetime

from django.conf import settings
#from main.basico.basico import Base 
import json,os,pytz,time,re
import subprocess as spp
import base64 as b64
import hashlib as hl
import openpyxl

# import excel
#from import_export.informacion import ImportExportModelInformacion
#import csv
##################################################
from django.http import StreamingHttpResponse
##################################################
import json,os,pytz,time,re,csv
# Create your views here.

NUMREGIS = 25


#BASE2 = Base.BASE2;
#BASE4 = Base.BASE4;
#BASE7 = Base.BASE7;
#BASE8 = Base.BASE8;
#BASE9 = Base.BASE9;


def index(request):
	return render(request, "main/index.html",{})

def iniciosesion(request):
	return render(request, "main/iniciosesion.html",{"iniciosesion":iniciosesion})


def indexprincipal(request):
	return render(request, "main/indexprincipal.html",{"indexprincipal":indexprincipal})

def usuarios (request):
	usuarios = Usuarios.objects.filter()
	informacion = Informacion.objects.filter()
	
	return render(request, "main/usuarios.html", {"usuarios":usuarios})

#def archivo (request):
	

def informacion(request):
	informacion = Informacion.objects.filter()
	return render(request, "main/informacion.html",{"informacion":informacion})


######################################-------inicio excel-------##########################################

#class Echo:

#	def write(self, value):
#		return	value
	
#	def some_streaming_csv_view(request):
		
#		rows = (["Row{}".format(idx), str(idx)] for idx in range(65536))
#		pseudo_buffer = Echo()
#		writer = csv.writer(pseudo_buffer)
#		response = StreamingHttpResponse((writer.writerow(row) for row in rows),
		
#		content_type="text/csv")
#		response['Content-Disposition'] = 'attachment';	
#		filename="somefilename.csv"
		
#			return response
		

######################################-------fin excel-------##########################################


######################################-------inicio cliente o registro del cliente-------##########################################


def guardarcliente(request):
	
	respon = json.loads(request.body.decode("utf8"))
	
	usuarios_id = respon["id"]
	nombres = respon["nombres"]
	apellidos = respon["apellidos"]
	correo = respon["correo"]
	usuario = respon["usuario"]
	contrasena = respon["contrasena"]


	usuariosCount = Usuarios.objects.filter(id=usuarios_id).count()
	respuesta={}
	
	if(usuariosCount > 0):
		usuarios = Usuarios.objects.get(id=usuarios_id)
		
		usuarios.nombres = nombres
		usuarios.apellidos = apellidos
		usuarios.correo = correo
		usuarios.usuario = usuario
		usuarios.contrasena = contrasena
				
		usuarios.save()
		respuesta= 3
	
	else:
		usuarios= Usuarios()

		usuarios.nombres = nombres
		usuarios.apellidos = apellidos
		usuarios.correo = correo
		usuarios.usuario = usuario
		usuarios.contrasena = contrasena

		
		usuarios.save()
			
		respuesta= 2
		
		return HttpResponse(
			json.dumps(respuesta),
			content_type="application/json"
		)
	
	
#######################################-------fin cliente o registro del cliente-------############################################

#############################################-------INICIO INFORMACION-------#####################################################

def guardarArchivo(request):
	#tabla orden trabajo
	#archivo
	
	respon = json.loads(request.body.decode("utf8"))
	
	usuarios_id = respon['usuarios_id']
	
	timezone.activate(pytz.timezone("America/Bogota"))
	hoy = str(timezone.localtime(timezone.now()))
	hoy = hoy[:19]
	hoy = datetime.strptime(hoy, "%Y-%m-%d %H:%M:%S")
	
	pub = hl.sha1()
	pub.update(str(time.time()).encode('utf8'))
	ale = pub.hexdigest()
	aleatorio= b64.b64encode(ale.encode('utf8')).decode('utf8')	
	usuarios = Usuarios.objects.filter(id=usuarios_id)
	
	if usuarios.exists():
		
		archivo = archivo()
		
		archivo.usuarios_id = usuarios[0].id
		archivo.fecha = hoy
		archivo.nombre_archivo = aleatorio+".xlsx"
		archivo.nombre_interno = aleatorio+".xlsx"
		archivo.numero_registro

		archivo.save()
		

	respuesta ={}
	respuesta['nombre_archivo'] = aleatorio

	return HttpResponse(
            json.dumps(respuesta),
            content_type="application/json"
        )


def guardarInformacion(request):
	#trabajo	
	#informacion
	
	respon = json.loads(request.body.decode("utf8"))
	archivo_id = respon['archivo_id']
	
	timezone.activate(pytz.timezone("America/Bogota"))
	hoy = str(timezone.localtime(timezone.now()))
	hoy = hoy[:19]
	hoy = datetime.strptime(hoy, "%Y-%m-%d %H:%M:%S")
	
	archivo = Archivo.objects.filter(id=archivo_id)
	
	if archivo.exists():

		archivo = Archivo.objects.get(id=archivo_id)
		
		documento = openpyxl.load_workbook(BASE7+archivo.nombre_archivo)
		hojas = documento.sheetnames
		
		hoja = documento[hojas[0]]
		registros =  hoja.rows
		contador = 0
		trabajos_id = []
		for fila in registros:
			contador = contador + 1
			if contador > 1:
				variables = {}
				for columna in fila:
					indice = re.sub("\d", "", columna.coordinate)
					variables[indice] = columna.value
				
					
				informacion = informacion()
				
				informacion.archivo_id = informacion_id
				informacion.fecha_inicio = hoy
				
				informacion.codigoEstacion = json.dumps(variables)
				informacion.nombreEstacion = json.dumps(variables)
				informacion.latitud = json.dumps(variables)
				informacion.longitud = json.dumps(variables)
				informacion.altitud = json.dumps(variables)
				informacion.categoria = json.dumps(variables)
				informacion.entidad = json.dumps(variables)
				informacion.areaOperativa = json.dumps(variables)
				informacion.departamento = json.dumps(variables)
				informacion.municipio = json.dumps(variables)
				informacion.fechaInstalacion = json.dumps(variables)
				informacion.fechaSuspension = json.dumps(variables)
				informacion.idParametro = json.dumps(variables)
				informacion.etiqueta = json.dumps(variables)
				informacion.descripcionSerie = json.dumps(variables)
				informacion.frecuencia = json.dumps(variables)
				informacion.fecha = json.dumps(variables)
				informacion.valor = json.dumps(variables)
				informacion.grado = json.dumps(variables)
				informacion.calificador = json.dumps(variables)
				informacion.nivelAprovacion = json.dumps(variables)
				
				informacion.save()

							
				informacion_id.append(informacion.id)
				
					
		archivo.save()
			
	respuesta ={}
	respuesta['informacion_id'] = informacion_id
	
	return HttpResponse(
            json.dumps(respuesta),
            content_type="application/json"
        )
	


@csrf_exempt
def guardarExcel(request):
	
	if(request.method == "POST"):

		action=request.POST["action"]

		if(action=="save"):

			upName=request.POST["upName"]
			upData=request.POST["upData"]
			

			
			f = open(BASE7+upName+"_ar.txt" ,"a")
			f.write(upData)
			f.close()
			return HttpResponse(upName, content_type="application/text")
		else:
			upName=request.POST["upName"]

			
			f = open(BASE7+upName+"_ar.txt")
			fotos = f.read();
			fotos = fotos.split('>>')
			
			del fotos[-1]
			for i in fotos:
				ar =i.split("<<")
				
				upData= ar[0]
				count = upData.count(",")

				if(count>0):

					posicion = upData.find(",")
					upData = upData[posicion+1:]
				if(len(ar)>2):
					nombre= upName+"_"+ar[1]+"."+ar[2]
				else:
					nombre= upName+ar[1]+".xlsx"
				f = open(BASE7+"v_"+nombre, "a")
				f.write(upData)
				f.close()
				
				spp.Popen(["python3", BASE4+"liserExcel.py", nombre, BASE7])
			
			os.remove(BASE7+upName+"_ar.txt")
			return HttpResponse(upName, content_type="application/text")































































#def guardarInformacion(request):

#	respon = json.loads(request.body.decode("utf8"))
	
#	informacion_id = respon["id"]
#	codigoEstacion = respon["codigoEstacion"]
#	nombreEstacion = respon["nombreEstacion"]
#	latitud = respon["latitud"]
#	longitud = respon["longitud"]
#	altitud = respon["altitud"]
#	categoria = respon["categoria"]
#	entidad = respon["entidad"]
#	areaOperativa = respon["areaOperativa"]
#	departamento = respon["departamento"]
#	municipio = respon["municipio"]
#	fechaInstalacion = respon["fechaInstalacion"]
#	fechaSuspension = respon["fechaSuspension"]
#	idParametro = respon["idParametro"]
#	etiqueta = respon["etiqueta"]
#	descripcionSerie = respon["descripcionSerie"]
#	frecuencia = respon["frecuencia"]
#	fecha = respon["fecha"]
#	valor = respon["valor"]
#	grado = respon["grado"]
#	calificador = respon["calificador"]
#	nivelAprovacion = respon["nivelAprovacion"]


#	informacionCount = Informacion.objects.filter(id=informacion_id).count()
#	respuesta={}
	
#	if(informacionCount > 0):
#		informacion = Informacion.objects.get(id=informacion_id)
#		informacion.codigoEstacion = codigoEstacion
#		informacion.nombreEstacion = nombreEstacion
#		informacion.latitud = latitud
#		informacion.longitud = longitud
#		informacion.altitud = altitud
#		informacion.categoria = categoria
#		informacion.entidad = entidad
#		informacion.areaOperativa = areaOperativa
#		informacion.departamento = departamento
#		informacion.municipio = municipio
#		informacion.fechaInstalacion = fechaInstalacion
#		informacion.fechaSuspension = fechaSuspension
#		informacion.idParametro = idParametro
#		informacion.etiqueta = etiqueta
#		informacion.descripcionSerie = descripcionSerie
#		informacion.frecuencia = frecuencia
#		informacion.fecha = fecha
#		informacion.valor = valor
#		informacion.grado = grado
#		informacion.calificador = calificador
#		informacion.nivelAprovacion = nivelAprovacion
		
#		informacion.save()
#		respuesta= 3
	
#	else:
#		informacion = Informacion()

#		informacion.codigoEstacion = codigoEstacion
#		informacion.nombreEstacion = nombreEstacion
#		informacion.latitud = latitud
#		informacion.longitud = longitud
#		informacion.altitud = altitud
#		informacion.categoria = categoria
#		informacion.entidad = entidad
#		informacion.areaOperativa = areaOperativa
#		informacion.departamento = departamento
#		informacion.municipio = municipio
#		informacion.fechaInstalacion = fechaInstalacion
#		informacion.fechaSuspension = fechaSuspension
#		informacion.idParametro = idParametro
#		informacion.etiqueta = etiqueta
#		informacion.descripcionSerie = descripcionSerie
#		informacion.frecuencia = frecuencia
#		informacion.fecha = fecha
#		informacion.valor = valor
#		informacion.grado = grado
#		informacion.calificador = calificador
#		informacion.nivelAprovacion = nivelAprovacion
		
#		informacion.save()
			
#		respuesta= 2
		
					
#	return HttpResponse(
#			json.dumps(respuesta),
#			content_type="application/json"
#		)

#def eliminarInformacion(request):

#	respon = json.loads(request.body.decode("utf8"))

#	informacion_id = respon["informacion_id"]
	
#	informacionCount = Informacion.objects.filter(id = informacion_id).count()
	
		
#	if(informacionCount > 0):
#		try:
#			informacion = Informacion.objects.get(id=informacion_id)
#			informacion.delete()
#			respuesta=2
#		except:

#			respuesta=3
			
#	else:

#		respuesta=1
		
		
#	return HttpResponse(
 #           json.dumps(respuesta),
  #          content_type="application/json"
   #     )

#############################################-------FIN DE INFORMACION-------########################################################


