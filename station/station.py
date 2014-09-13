from container.container import Container

class Station(Container):

	def __init__(self):
		self.bikes = []
		self.capacity = 5
		self.available_bikes = []
		self.broken_bikes = []