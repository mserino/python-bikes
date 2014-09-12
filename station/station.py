class Station(object):

	def __init__(self):
		self.bikes = []
		self.capacity = 5
		self.broken_bikes = []
		self.available_bikes = []

	def dock(self, bike):
		if self.is_full() == "full":
			return "Cannot dock any more bikes"
		elif self.has_already(bike):
			return "Cannot dock the same bike twice"
		else:
			self.bikes.append(bike)

		if bike.broken:
			self.broken_bikes.append(bike)
		else:
			self.available_bikes.append(bike)

	def release(self, bike):
		self.bikes.remove(bike)

	def is_full(self):
		if len(self.bikes) == self.capacity:
			return "full"
		else:
			return "not full"

	def has_already(self, bike):
		if bike in self.bikes:
			return True