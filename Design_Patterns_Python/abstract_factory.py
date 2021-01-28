#Design Pattern: Abstract Factory

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

class Abstracts_Factory:
	#abstarcts details of objects of a facotry i.e. here get_num_wheels()
	def __init__(self,vehicle):
		self.vehicle=vehicle

	def get_details(self):
		self.vehicle.get_num_wheels()

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
		Abstracts_Factory(vehicle_factory(vehicle)).get_details()
