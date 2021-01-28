#Design Pattern: Builder

class Vehicle:
	def __init__(self):
		self.wheels=2
	
	def get_num_wheels(self):
		print(self.wheels)

	

class Bike(Vehicle):
	def __init__(self):
		super().__init__() 
		self.wheels=2

class Car(Vehicle):
	def __init__(self):
		super().__init__() 
		self.wheels=4

class Trike(Vehicle):
	def __init__(self):
		super().__init__() 
		self.wheels=3


class Vehicle_Builder:
	def __init__(self):
		self.wheels=6
	def get_num_wheels(self):
		pass


class Build_Vehicle(Vehicle_Builder):
	def get_num_wheels(self):
		print(self.wheels)

def create_vehicle(cls):
	vehicle=cls()
	vehicle.wheels=4
	return vehicle


if __name__ == '__main__':


	bike=Bike()
	car=Car()
	trike=Trike()
	quadra=create_vehicle(Build_Vehicle)


	vehicles=[bike,car,trike,quadra]

	for vehicle in vehicles:
		vehicle.get_num_wheels()
