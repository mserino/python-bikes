from nose.tools import *
import nose
from person.person import Person
from bike.bike import Bike
from station.station import Station

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
		self.station = Station()

	def teardown(self):
		"""This method is run once after _each_ test method is executed"""
		pass
	
	def test_person_has_no_bikes(self):
		assert_equal(len(self.person.bikes), 0)

	def test_person_can_have_a_bike(self):
		self.person.rides(self.bike)
		assert_equal(len(self.person.bikes), 1)
		assert_in(self.bike, self.person.bikes)

	def test_person_can_release_a_bike(self):
		self.person.rides(self.bike)
		self.person.release(self.bike)
		assert_equal(len(self.person.bikes), 0)

	def test_person_can_have_only_one_bike(self):
		assert_equal(self.person.capacity, 1)

	def test_person_is_not_full(self):
		assert_equal(self.person.has_bike(), "doesn\'t have any bike")

	def test_person_has_a_bike(self):
		self.person.rides(self.bike)
		assert_equal(self.person.has_bike(), "has one bike")

	def test_person_cannot_have_two_bikes(self):
		self.person.rides(self.bike)
		self.person.rides(self.bike2)
		assert_equal(self.person.rides(self.bike2), "Cannot ride more than one bike")

	def test_person_falls_and_bike_is_broken(self):
		self.person.rides(self.bike)
		self.person.falls_from(self.bike)
		assert_true(self.bike.broken)

	def test_person_cannot_rent_if_station_has_no_bikes(self):
		assert_equal(self.person.rent_from(self.bike, self.station), "There are no bikes here")

	def test_person_can_rent_bike_from_station(self):
		self.station.dock(self.bike)
		self.person.rent_from(self.bike, self.station)
		assert_in(self.bike, self.person.bikes)
		assert_not_in(self.bike, self.station.bikes)
