
''' informacion clubfit '''

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'basico'))
from basico import Base


class tools():

	LOG = ""
	
	def __init__(self, mensaje):
		pass
	
	def set_log(self,trabajo_id, mensaje):
		print("################")
		
		print(mensaje)
		log = open(Base.BASE9+str(trabajo_id)+".txt","w") 
		log.write("|"+mensaje) 
		log.close() 
		return True
	
	def get_log(self,trabajo_id):
		log = open (Base.BASE9+str(trabajo_id)+".txt" , "r")  
		log = log.read() 
		return str(log)
		
	
