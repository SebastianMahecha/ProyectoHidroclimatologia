
''' informacion clubfit '''

#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options
 

from tools import tools
import sys,json,requests

class Robot:
	def __init__(self):

		self.BASE4 = sys.argv[1]
		self.VARIABLES = json.loads(sys.argv[2])
		self.TRABAJO_ID = json.loads(sys.argv[3])

	def run_robot(self):
		try:
			
			tools.set_log(self,self.TRABAJO_ID,"hola")
			#tools.set_log(self,"cuando")
			#print(tools.get_log(self))
			
			chrome_options = Options()
			#argument to switch off suid sandBox and no sandBox in Chrome 
			chrome_options.add_argument('--dns-prefetch-disable')
			chrome_options.add_argument("--no-sandbox")
			chrome_options.add_argument("--disable-setuid-sandbox")
			chrome_options.add_argument('--lang=en-US')
			chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en-US'})
			
			driver = webdriver.Chrome(self.BASE4+"chromedriver/chromedriver", chrome_options=chrome_options)
			driver.get("https://www.facebook.com/")
			
			driver.find_element_by_id("email").send_keys("310861536")
			driver.find_element_by_name("pass").send_keys("hjhj")
			driver.find_element_by_id("u_0_3").click()

			driver.close()
			estado = 0
			mensaje = 'Robot ejecutado correctamente'
		except Exception as e:
			estado = 1
			mensaje = e
		
		self.responder(estado, mensaje)

	def responder(self, estado, mensaje):
		
		datos= {'clave': 'PQu4GJyOAuICd8cWA2xpcxnC8GpWeToT35KCwxNEdN3HTGIg',
				'estado': estado,
				'mensaje': mensaje,
				'trabajo_id': self.TRABAJO_ID,
				'log': tools.get_log(self,self.TRABAJO_ID)
				}

		r = requests.post('https://127.0.0.1:9080/main/respuestaRobot/', verify=False,  data=datos)


robot = Robot()
robot.run_robot()
