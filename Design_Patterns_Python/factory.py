#Design Pattern: Factory

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

def vehicle_factory(key='Bike'):

	vehicle_dict = {
	'Bike':Bike(),
	'Car':Car(),
	'Trike':Trike()
	}

	return vehicle_dict[key]


if __name__ == '__main__':

	vehicles=['Bike','Trike','Car']

	for vehicle in vehicles:
		vehicle_factory(vehicle).get_num_wheels()
