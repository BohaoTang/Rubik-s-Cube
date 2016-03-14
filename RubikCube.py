import numpy as np
import matplotlib.pyplot as plt 

class RubikCube():
	faces = ['u','r','f','d','l','b']
	positions = ['u','r','f','d','l','b','e','m','s']
	status = {}

	# initialize a rubik's cube
	def __init__(self):
		
	
	#foundemantal rotations
	def U(self):
		pass
	def Uinv(self):
		pass	
	def R(self):
		pass
	def Rinv(self):
		pass
	def F(self):
		pass
	def Finv(self):
		pass
	def D(self):
		pass
	def Dinv(self):
		pass			
	def L(self):
		pass
	def Linv(self):
		pass	
	def B(self):
		pass
	def Binv(self):
		pass	
	def E(self):
		pass
	def Einv(self):
		pass
	def M(self):
		pass
	def Minv(self):
		pass	
	def S(self):
		pass
	def Sinv(self):
		pass

	#transform from a formula
	def formula(self, fstr):
		pass

	#change status arbitrarily
	def set(self, status):
		pass

	#focus on some certain blocks
	def focus(self, points):
		pass

	#show
	def show(self,color=['y','b','r','bk','g','o'],notation=None,exfaces=None,\
			 movement=None,arrow=None,dimension=3):
		pass

	#show a formula
	def fshow(self,color='default',formula=None,notation=None,dimension=3):
		pass
