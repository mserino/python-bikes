import unittest
from bike import Bike

class BikeTest(unittest.TestCase):

	def setUp(self):
		self.bike = Bike()

	def test_bike_not_broken(self):
		self.assertFalse(self.bike.broken)

	def test_bike_can_be_broken(self):
		self.bike.break_bike()
		self.assertTrue(self.bike.broken)

	def test_bike_can_be_fixed(self):
		self.bike.break_bike()
		self.bike.fix_bike()
		self.assertFalse(self.bike.broken)

	def test_fixed_status_of_the_bike_when_created(self):
		self.assertEqual(self.bike.status, "fixed")

	def test_broken_status_of_the_bike_when_broken(self):
		self.bike.break_bike()
		self.assertEqual(self.bike.status, "broken")

	def test_fixed_status_of_the_bike_when_fixed(self):
		self.bike.break_bike()
		self.bike.fix_bike()
		self.assertEqual(self.bike.status, "fixed")

if __name__ == '__main__':
	unittest.main()