class Bike(object):
	
	def __init__(self):
		self.broken = False
		self.status = "fixed"

	def break_bike(self):
		self.broken = True
		self.status = "broken"

	def fix_bike(self):
		self.broken = False
		self.status = "fixed"