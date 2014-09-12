class Person(object):

	def __init__(self):
		self.bikes = []
		self.capacity = 1

	def rides(self, bike):
		if self.has_bike() == "doesn\'t have any bike":
			self.bikes.append(bike)
		else:
			return "Cannot ride more than one bike"

	def release(self, bike):
		self.bikes.remove(bike)

	def has_bike(self):
		if len(self.bikes) < self.capacity:
			return "doesn\'t have any bike"
		else:
			return "has one bike"

	def falls_from(self, bike):
		bike.broken = True