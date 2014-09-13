class Container:
	def __init__(self, capacity):
		self.bikes = []
		self.capacity = capacity
		self.broken_bikes = []
		self.available_bikes = []

	def dock(self, bike):
		if self.is_full() == "full":
			return "Cannot dock any more bikes"
		elif self.has_already(bike):
			return "Cannot dock the same bike twice"
		else:
			self.bikes.append(bike)

		# broken bikes
		if bike.broken:
			self.broken_bikes.append(bike)
		# available bikes
		else:
			self.available_bikes.append(bike)

	def release(self, bike):
		if bike in self.bikes:
			self.bikes.remove(bike)
		else:
			return "There are no bikes here"

	def is_full(self):
		if len(self.bikes) == self.capacity:
			return "full"
		else:
			return "not full"

	def has_already(self, bike):
		if bike in self.bikes:
			return True