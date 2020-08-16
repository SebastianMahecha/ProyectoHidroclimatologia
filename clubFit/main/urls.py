
from django.urls import path

from . import views

 

from django.urls import include,path
#from django.contrib.auth.view import login,logout_then_login


urlpatterns = [
    path('', views.index, name='index'),
    #path('',login,{'template_name':'iniciosesion.html'}, name= 'login'),
    
    path('indexprincipal', views.indexprincipal, name='indexprincipal'),
    
    ################################ ---INICIO DE CLIENTES ---######################################
	path('usuarios', views.usuarios, name='usuarios'),
	path('guardarcliente', views.guardarcliente, name='guardarcliente'),
	
	################################ ---FIN DE CLIENTES ---#########################################
    ################################ ---INICIO DE INICIO DE SESION ---######################################
    
	path('iniciosesion', views.iniciosesion, name='iniciosesion'),
    
    
    ################################ ---FIN DE INICIO DE SESION ---######################################
	#############################---INICIO DE INFORMACION ---######################################
    
	path('informacion', views.informacion, name='informacion'),
	path('guardarArchivo', views.guardarArchivo, name='guardarArchivo'),
	path('guardarInformacion', views.guardarInformacion, name='guardarInformacion'),
	path('guardarExcel', views.guardarExcel, name='guardarExcel')
	
	#############################---FIN DE INFORMACION---#########################################    
    
    
   
]

