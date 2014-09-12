from nose.tools import *
import nose
from person import Person
from bike import Bike

class TestPerson(object):

	@classmethod
	def setup_class(klass):
		"""This method is run once for each class before any tests are run"""

	@classmethod
	def teardown_class(klass):
		"""This method is run once for each class _after_ all tests are run"""

	def setUp(self):
		"""This method is run once before _each_ test method is executed"""
		self.person = Person()
		self.bike = Bike()
		self.bike2 = Bike()

	def teardown(self):
		"""This method is run once after _each_ test method is executed"""
		pass
	
	def test_person_has_no_bikes(self):
		assert_equal(len(self.person.bikes), 0)

	def test_person_can_have_a_bike(self):
		self.person.dock(self.bike)
		assert_equal(len(self.person.bikes), 1)
		assert_in(self.bike, self.person.bikes)

	def test_person_can_release_a_bike(self):
		self.person.dock(self.bike)
		self.person.release(self.bike)
		assert_equal(len(self.person.bikes), 0)

	def test_person_can_have_only_one_bike(self):
		assert_equal(self.person.capacity, 1)

	def test_person_is_not_full(self):
		assert_equal(self.person.is_full(), "not full")

	def test_person_is_full(self):
		self.person.dock(self.bike)
		assert_equal(self.person.is_full(), "full")

	def test_person_cannot_have_another_bike_if_full(self):
		self.person.dock(self.bike)
		self.person.dock(self.bike2)
		assert_equal(self.person.dock(self.bike2), "Cannot dock more than one bike")

if __name__ == '__main__':
	unittest.main()