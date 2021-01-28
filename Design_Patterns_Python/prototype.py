#Design Pattern: Prototype

import copy

class Shapes:

	def __init__(self):
		self.type='shape'

	def get_type(self):
		return self.type

	def get_area(self):
		pass

	def clone(self):
		return copy.copy(self)

class Circle(Shapes):

	def __init__(self,radius):
		super().__init__()
		self.type='circle'
		self.radius=radius

	def get_area(self):
		return 3.14*self.radius*self.radius

class Square(Shapes):

	def __init__(self,side):
		super().__init__()
		self.type='square'
		self.side=side

	def get_area(self):
		return self.side*self.side

class Rectangle(Shapes):

	def __init__(self,leng,brea):
		super().__init__()
		self.type='rectangle'
		self.leng=leng
		self.brea=brea


	def get_area(self):
		return self.leng*self.brea

class Shapes_Prototype:
	obj_dict={} #class variable
	@staticmethod
	def get_shape(key):
		return Shapes_Prototype.obj_dict[key].clone()

	@staticmethod
	def load(radius,side,leng,brea):

		circ=Circle(radius)
		Shapes_Prototype.obj_dict['c']=circ

		squr=Square(side)
		Shapes_Prototype.obj_dict['s']=squr

		rect=Rectangle(leng,brea)
		Shapes_Prototype.obj_dict['r']=rect


if __name__ == '__main__':

	Shapes_Prototype.load(radius=5,side=4,leng=3,brea=2)

	circ=Shapes_Prototype.get_shape('c')
	print(isinstance(circ,Circle))
	print(circ.get_type(),circ.get_area())
	squr=Shapes_Prototype.get_shape('s')
	print(squr.get_type(),squr.get_area())
	rect=Shapes_Prototype.get_shape('r')
	print(rect.get_type(),rect.get_area())


