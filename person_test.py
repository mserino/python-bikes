import unittest
from person import Person
from bike import Bike

class PersonTest(unittest.TestCase):

	def setUp(self):
		self.person = Person()
		self.bike = Bike()

	def test_person_has_no_bikes(self):
		for bike in self.person.bikes:
			self.assertEqual(self.person.bikes.count(bike), 0)

	def test_person_can_have_a_bike(self):
		self.person.dock(self.bike)
		for bike in self.person.bikes:
			self.assertEqual(self.person.bikes.count(bike), 1)

if __name__ == '__main__':
	unittest.main()