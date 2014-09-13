from nose.tools import *
import nose
from garage.garage import Garage
from bike.bike import Bike

class TestVan(object):

	@classmethod
	def setup_class(klass):
		"""This method is run once for each class before any tests are run"""

	@classmethod
	def teardown_class(klass):
		"""This method is run once for each class _after_ all tests are run"""

	def setUp(self):
		"""This method is run once before _each_ test method is executed"""
		self.garage = Garage()
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

	def test_garage_has_capacity_of_six(self):
		assert_equal(self.garage.capacity, 6)

	def test_garage_is_not_full(self):
		self.garage.dock(self.bike)
		self.garage.dock(self.bike2)
		assert_equal(self.garage.is_full(), "not full")

	def test_garage_can_be_full(self):
		self.garage.dock(self.bike)
		self.garage.dock(self.bike2)
		self.garage.dock(self.bike3)
		self.garage.dock(self.bike4)
		self.garage.dock(self.bike5)
		self.garage.dock(self.bike6)
		assert_equal(self.garage.is_full(), "full")

	def test_garage_cannot_dock_more_than_five_bikes(self):
		self.garage.dock(self.bike)
		self.garage.dock(self.bike2)
		self.garage.dock(self.bike3)
		self.garage.dock(self.bike4)
		self.garage.dock(self.bike5)
		self.garage.dock(self.bike6)
		assert_equal(self.garage.dock(self.bike7), "Cannot dock any more bikes")

	def test_can_fix_one_broken_bike(self):
		self.bike.break_bike()
		self.garage.dock(self.bike)
		self.garage.fix_bikes()
		assert_in(self.bike, self.garage.available_bikes)

	def test_can_fix_all_broken_bikes(self):
		self.bike.break_bike()
		self.bike2.break_bike()
		self.garage.dock(self.bike)
		self.garage.dock(self.bike2)
		self.garage.fix_bikes()
		assert_in(self.bike, self.garage.available_bikes)
		assert_in(self.bike2, self.garage.available_bikes)