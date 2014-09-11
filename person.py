class Person(object):

	def __init__(self):
		self.bikes = []

	def dock(self, bike):
		self.bikes.append(bike)