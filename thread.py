from threading import Thread, RLock
import time

verrou = RLock()

class IaThread(Thread):
	
	def __init__(self):
        Thread.__init__(self)
		self.result = None
		
	def run(self):
		pass
		#Quand on voudra accéder à la ressource partagée :
		with verrou:
			