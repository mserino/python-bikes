import unittest
from bike import Bike

class BikeTest(unittest.TestCase):

	def setUp(self):
		self.bike = Bike()

	def test_not_broken(self):
		self.assertFalse(self.bike.broken)

	def test_bike_breaks(self):
		self.bike.break_bike()
		self.assertTrue(self.bike.broken)

	def test_bike_can_be_fixed(self):
		self.bike.break_bike()
		self.bike.fix_bike()
		self.assertFalse(self.bike.broken)

if __name__ == '__main__':
	unittest.main()