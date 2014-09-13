from container.container import Container

class Van(Container):
	def __init__(self):
		self.bikes = []
		self.capacity = 10
		self.available_bikes = []
		self.broken_bikes = []