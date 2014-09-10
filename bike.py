class Bike(object):
	broken = False

	def break_bike(self):
		self.broken = True

	def fix_bike(self):
		self.broken = False