from container.container import Container
class Garage(Container):
	
	def __init__(self):
		self.capacity = 6
		self.bikes = []
		self.available_bikes = []
		self.broken_bikes = []

	def fix_bikes(self):
		if len(self.broken_bikes) > 0:
			for bike in self.broken_bikes:
				bike.fix_bike()
				self.available_bikes.append(bike)
		else:
			return "There are no broken bikes here"

		for bike in self.available_bikes:
			self.broken_bikes.remove(bike)