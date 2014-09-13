class Person(object):

	def __init__(self):
		self.bikes = []
		self.capacity = 1

	def rides(self, bike):
		if self.has_bike() == "doesn\'t have any bike":
			if bike.broken == True:
				return "Cannot ride a broken bike"
			else:
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

	def rent_from(self, bike, station):
		if bike in station.bikes:
			if bike.broken == True:
				return "This bike is broken"
			else:
				station.release(bike)
				self.rides(bike)
		else:
			return "There are no bikes here"

	def return_to(self, bike, station):
		self.release(bike)
		station.dock(bike)