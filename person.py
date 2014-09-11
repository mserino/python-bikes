class Person(object):

	def __init__(self):
		self.bikes = []
		self.capacity = 1

	def dock(self, bike):
		if len(self.bikes) < self.capacity:
			self.bikes.append(bike)
		else:
			return "Cannot dock more than one bike"

	def release(self, bike):
		self.bikes.remove(bike)

	def is_full(self):
		if self.capacity == len(self.bikes):
			return "full"
		else:
			return "not full"