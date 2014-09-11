import unittest
from person import Person
from bike import Bike

class PersonTest(unittest.TestCase):

	def setUp(self):
		self.person = Person()
		self.bike = Bike()
		self.bike2 = Bike()
	
	def test_person_has_no_bikes(self):
		self.assertEqual(len(self.person.bikes), 0)

	def test_person_can_have_a_bike(self):
		self.person.dock(self.bike)
		self.assertEqual(len(self.person.bikes), 1)
		self.assertIn(self.bike, self.person.bikes)

	def test_person_can_release_a_bike(self):
		self.person.dock(self.bike)
		self.person.release(self.bike)
		self.assertEqual(len(self.person.bikes), 0)

	def test_person_can_have_only_one_bike(self):
		self.assertEqual(self.person.capacity, 1)

	def test_person_is_not_full(self):
		self.assertEqual(self.person.is_full(), "not full")

	def test_person_is_full(self):
		self.person.dock(self.bike)
		self.assertEqual(self.person.is_full(), "full")

	def test_person_cannot_have_another_bike_if_full(self):
		self.person.dock(self.bike)
		self.person.dock(self.bike2)
		self.assertEqual(self.person.dock(self.bike2), "Cannot dock more than one bike")

if __name__ == '__main__':
	unittest.main()