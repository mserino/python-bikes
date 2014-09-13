from nose.tools import *
import nose
from container.container import Container
from bike.bike import Bike

class TestContainer(object):

	@classmethod
	def setup_class(klass):
		"""This method is run once for each class before any tests are run"""

	@classmethod
	def teardown_class(klass):
		"""This method is run once for each class _after_ all tests are run"""

	def setUp(self):
		"""This method is run once before _each_ test method is executed"""
		self.container = Container(6)
		self.other_container = Container(5)
		self.bike = Bike()
		self.bike2 = Bike()
		self.bike3 = Bike()
		self.bike4 = Bike()
		self.bike5 = Bike()
		self.bike6 = Bike()
		self.bike7 = Bike()

	def teardown(self):
		"""This method is run once after _each_ test method is executed"""
		pass
	
	def test_container_has_no_bikes(self):
		assert_equal(len(self.container.bikes), 0)

	def test_container_can_have_a_bike(self):
		self.container.dock(self.bike)
		assert_equal(len(self.container.bikes), 1)
		assert_in(self.bike, self.container.bikes)

	def test_container_can_release_a_bike(self):
		self.container.dock(self.bike)
		self.container.release(self.bike)
		assert_equal(len(self.container.bikes), 0)

	def test_container_can_release_a_bike_if_has_one(self):
		assert_equal(self.container.release(self.bike), "There are no bikes here")

	def test_container_has_a_maximum_capacity(self):
		assert_equal(self.container.capacity, 6)

	def test_container_is_not_full(self):
		self.container.dock(self.bike)
		self.container.dock(self.bike2)
		assert_equal(self.container.is_full(), "not full")

	def test_container_can_be_full(self):
		self.container.dock(self.bike)
		self.container.dock(self.bike2)
		self.container.dock(self.bike3)
		self.container.dock(self.bike4)
		self.container.dock(self.bike5)
		self.container.dock(self.bike6)
		assert_equal(self.container.is_full(), "full")

	def test_container_cannot_dock_more_than_six_bikes(self):
		self.container.dock(self.bike)
		self.container.dock(self.bike2)
		self.container.dock(self.bike3)
		self.container.dock(self.bike4)
		self.container.dock(self.bike5)
		self.container.dock(self.bike6)
		assert_equal(self.container.dock(self.bike7), "Cannot dock any more bikes")

	def test_container_has_broken_bikes(self):
		self.bike.break_bike()
		self.container.dock(self.bike)
		self.container.dock(self.bike2)
		assert_in(self.bike, self.container.broken_bikes)

	def test_container_has_available_bikes(self):
		self.container.dock(self.bike)
		self.container.dock(self.bike2)
		assert_in(self.bike, self.container.available_bikes)
		assert_in(self.bike2, self.container.available_bikes)

	def test_if_a_bike_is_already_docked(self):
		self.container.dock(self.bike)
		assert_true(self.container.has_already(self.bike))

	def test_bike_cannot_be_docked_twice(self):
		self.container.dock(self.bike)
		assert_equal(self.container.dock(self.bike), "Cannot dock the same bike twice")

	def test_can_release_all_broken_bikes(self):
		self.bike.break_bike()
		self.bike2.break_bike()
		self.container.dock(self.bike)
		self.container.dock(self.bike2)
		self.container.release_broken_bikes(self.other_container)
		assert_in(self.bike, self.other_container.bikes)
		assert_in(self.bike2, self.other_container.bikes)
		assert_not_in(self.bike, self.container.bikes)
		assert_not_in(self.bike2, self.container.bikes)

	def test_error_message_if_no_broken_bikes(self):
		self.container.dock(self.bike)
		assert_equal(self.container.release_broken_bikes(self.other_container), "There are no broken bikes here")

	def test_can_release_all_available_bikes(self):
		self.container.dock(self.bike)
		self.container.dock(self.bike2)
		self.container.release_available_bikes(self.other_container)
		assert_in(self.bike, self.other_container.bikes)
		assert_in(self.bike2, self.other_container.bikes)
		assert_not_in(self.bike, self.container.bikes)
		assert_not_in(self.bike2, self.container.bikes)


	def test_error_message_if_no_available_bikes(self):
		self.bike.break_bike()
		self.container.dock(self.bike)
		assert_equal(self.container.release_available_bikes(self.other_container), "There are no available bikes here")