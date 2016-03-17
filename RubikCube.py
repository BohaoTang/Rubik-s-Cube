import numpy as np
import matplotlib.pyplot as plt 

class RubikCube():
'''
	from RubikCube import RubikCube
	cube = RubikCube()
	cube.show() to show the cube
	cube.do('act') to do a rotation, 
	act is showed in picture n1.jpg
	cube.formula() to transform from a formula
	formula is like "act act act" 
	the cube will show itself whenever you transform it 
'''

	status = {}
	
	faces = ['u','r','f','d','l','b']
	positions = {'u':['lmr','bsf'],\
				 'r':['fsb','ued'],\
				 'f':['lmr','ued'],\
				 'd':['lmr','bsf'],\
				 'l':['fsb','ued'],\
				 'b':['lmr','ued']}	
	zipdict = {'up':[1,0],'right':[0,2],'down':[1,2],'left':[0,0]}
	direction = {'U':0,'R':0,'F':0,'D':1,'L':1,'B':1,'E':0,'M':0,'S':1}
	
	coordinate = []

	# initialize a rubik's cube
	def __init__(self):
		for face in self.faces:
			for y in self.positions[face][1]:
				for x in self.positions[face][0]:
					self.coordinate.append(face+x+y)
		for co in self.coordinate:
			self.status[co] = co
		self.coordinate = np.array(self.coordinate).reshape(6,3,3)
		

	#foundemantal rotations
	def zipblocks(self,face):
		uedge = self.coordinate[self.faces.index(face)][0,:]
		zipface = self.positions[face][self.zipdict['up'][0]][self.zipdict['up'][1]]
		zipface = self.coordinate[self.faces.index(zipface)].reshape(9)
		uedgeAUX = []
		for x in uedge:
			for y in zipface:
				if set(x) == set(y):
					uedgeAUX.append(y)
		uedge = zip(uedge,uedgeAUX)

		redge = self.coordinate[self.faces.index(face)][:,2]
		zipface = self.positions[face][self.zipdict['right'][0]][self.zipdict['right'][1]]
		zipface = self.coordinate[self.faces.index(zipface)].reshape(9)
		redgeAUX = []
		for x in redge:
			for y in zipface:
				if set(x) == set(y):
					redgeAUX.append(y)
		redge = zip(redge,redgeAUX)

		dedge = self.coordinate[self.faces.index(face)][2,:][::-1]
		zipface = self.positions[face][self.zipdict['down'][0]][self.zipdict['down'][1]]
		zipface = self.coordinate[self.faces.index(zipface)].reshape(9)
		dedgeAUX = []
		for x in dedge:
			for y in zipface:
				if set(x) == set(y):
					dedgeAUX.append(y)
		dedge = zip(dedge,dedgeAUX)

		ledge = self.coordinate[self.faces.index(face)][:,0][::-1]
		zipface = self.positions[face][self.zipdict['left'][0]][self.zipdict['left'][1]]
		zipface = self.coordinate[self.faces.index(zipface)].reshape(9)
		ledgeAUX = []
		for x in ledge:
			for y in zipface:
				if set(x) == set(y):
					ledgeAUX.append(y)
		ledge = zip(ledge,ledgeAUX)
		return uedge,redge,dedge,ledge

	def find_middle(self,pos):
		blocks = []
		for x in self.coordinate:
			for y in x:
				for z in y:
					if pos in z:
						blocks.append(z)
		blocks = np.array(blocks).reshape(4,3)
		a = blocks[0]
		b = blocks[1]
		c = blocks[2][::-1]
		d = blocks[3][::-1]
		return a,b,c,d

	#0 for clockwise, 1 for counterclockwise
	def edge_rotate(self,uedge,redge,dedge,ledge,direction):
		if not direction:
			for i in range(3):
				for j in range(2):
					self.status[uedge[i][j]],self.status[redge[i][j]],\
					self.status[dedge[i][j]],self.status[ledge[i][j]] = \
					self.status[ledge[i][j]],self.status[uedge[i][j]],\
					self.status[redge[i][j]],self.status[dedge[i][j]]
		else:
			for i in range(3):
				for j in range(2):
					self.status[uedge[i][j]],self.status[redge[i][j]],\
					self.status[dedge[i][j]],self.status[ledge[i][j]] = \
					self.status[redge[i][j]],self.status[dedge[i][j]],\
					self.status[ledge[i][j]],self.status[uedge[i][j]]
					

	def middle_rotate(self,a,b,c,d,direction):
		if not direction:
			for i in range(3):
				self.status[a[i]],self.status[b[i]],self.status[c[i]],self.status[d[i]] = \
				self.status[d[i]],self.status[a[i]],self.status[b[i]],self.status[c[i]]
		else:
			for i in range(3):
				self.status[a[i]],self.status[b[i]],self.status[c[i]],self.status[d[i]] = \
				self.status[b[i]],self.status[c[i]],self.status[d[i]],self.status[a[i]]

	def do(self,act,ifshow = 1):
		if len(act) > 2: 
			raise(ValueError('the action is illegal'))
		if len(act) == 2 and act[1] not in ["2","'"]: 
			raise(ValueError('the action is illegal'))
		if len(act) == 2 and act[1] == '2':
			self.do(act[0],ifshow = 0)
			self.do(act[0],ifshow)
		elif act[0] in ['U','R','F','D','L','B']:
			uedge,redge,dedge,ledge = self.zipblocks(act[0].lower())
			self.edge_rotate(uedge,redge,dedge,ledge, self.direction[act[0]]^(len(act)-1))
			if ifshow: self.show()
		elif act[0] in ['E','M','S']:
			a,b,c,d = self.find_middle(act[0].lower()) 
			self.middle_rotate(a,b,c,d, self.direction[act[0]]^(len(act)-1))
			if ifshow: self.show()
		else: raise(ValueError('the action is illegal'))

	#transform from a formula
	def formula(self, fstr):
		formulas = fstr.split()
		for act in formulas:
			self.do(act,ifshow=0)
		self.show()

	#change status arbitrarily
	def set(self, status):
		pass

	#focus on some certain blocks
	def focus(self, points):
		pass

	#show
	def show(self,color=['y','b','r','bk','g','o'],notation=None,exfaces=None,\
			 movement=None,arrow=None,dimension=3):
		cube = [self.status[x][0] for x in self.coordinate.reshape(54)]
		cube = np.array(cube).reshape(6,3,3)
		print cube

	#show a formula
	def fshow(self,color='default',formula=None,notation=None,dimension=3):
		pass
