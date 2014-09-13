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

	def release_and_dock(self, bikes, other_container):
		for bike in bikes:
			self.release(bike)
			other_container.dock(bike)

	def release_broken_bikes(self, other_container):
		if len(self.broken_bikes) > 0:
			self.release_and_dock(self.broken_bikes, other_container)
		else:
			return "There are no broken bikes here"

	def release_available_bikes(self, other_container):
		if len(self.available_bikes) > 0:
			self.release_and_dock(self.available_bikes, other_container)
		else:
			return "There are no available bikes here"