#Design Pattern: Singleton

class Auto:
	__instance=None #private variable

	@staticmethod  #use of static method independent of 
	def get_instance():

		if Auto.__instance == None:
			Auto()
		return Auto.__instance

	def __init__(self):

		if Auto.__instance != None:
			raise Exception("This class is a Singleton") #cannot create new objects
		else:
			Auto.__instance=self
		

		self.state='CAR'

	def __str__(self):
		return self.state

if __name__=='__main__':

	car=Auto()
	# car2=Auto()

	honda=Auto.get_instance()
	tata=Auto.get_instance()

	tata.state='4 wheeler'
	print(f'car = {car}, honda = {honda},tata = {tata}')
	
	print(f'honda is car: {honda is car}')
	print(f'tata is car: {tata is car}')
	print(f'tata is honda: {tata is honda}')
	# print(f'car is car2: {car is car2}')


	

