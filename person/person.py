class Person(object):

	def __init__(self):
		self.bikes = []
		self.capacity = 1

	def rides(self, bike):
		if self.is_full() == "not full":
			self.bikes.append(bike)
		else:
			return "Cannot ride more than one bike"

	def release(self, bike):
		self.bikes.remove(bike)

	def is_full(self):
		if self.capacity == len(self.bikes):
			return "full"
		else:
			return "not full"

	def falls_from(self, bike):
		bike.broken = True