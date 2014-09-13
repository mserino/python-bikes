from container.container import Container
class Garage(Container):
	
	def __init__(self):
		self.capacity = 6
		self.bikes = []
		self.available_bikes = []
		self.broken_bikes = []

	def fix_bikes(self):
		for bike in self.broken_bikes:
			bike.fix_bike()
			self.available_bikes.append(bike)
			
		for bike in self.available_bikes:
			self.broken_bikes.remove(bike)