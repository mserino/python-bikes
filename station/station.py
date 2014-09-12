class Station(object):

	def __init__(self):
		self.bikes = []
		self.capacity = 5

	def dock(self, bike):
		if len(self.bikes) < self.capacity:
			self.bikes.append(bike)
		else:
			return "Cannot dock any more bikes"

	def release(self, bike):
		self.bikes.remove(bike)