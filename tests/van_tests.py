from nose.tools import *
import nose
from van.van import Van
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
		self.van = Van()
		self.bike = Bike()
		self.bike2 = Bike()
		self.bike3 = Bike()
		self.bike4 = Bike()
		self.bike5 = Bike()
		self.bike6 = Bike()
		self.bike7 = Bike()
		self.bike8 = Bike()
		self.bike9 = Bike()
		self.bike10 = Bike()
		self.bike11 = Bike()

	def teardown(self):
		"""This method is run once after _each_ test method is executed"""
		pass

	def test_van_has_capacity_of_ten(self):
		assert_equal(self.van.capacity, 10)

	def test_van_is_not_full(self):
		self.van.dock(self.bike)
		self.van.dock(self.bike2)
		assert_equal(self.van.is_full(), "not full")

	def test_van_can_be_full(self):
		self.van.dock(self.bike)
		self.van.dock(self.bike2)
		self.van.dock(self.bike3)
		self.van.dock(self.bike4)
		self.van.dock(self.bike5)
		self.van.dock(self.bike6)
		self.van.dock(self.bike7)
		self.van.dock(self.bike8)
		self.van.dock(self.bike9)
		self.van.dock(self.bike10)
		assert_equal(self.van.is_full(), "full")

	def test_van_cannot_dock_more_than_five_bikes(self):
		self.van.dock(self.bike)
		self.van.dock(self.bike2)
		self.van.dock(self.bike3)
		self.van.dock(self.bike4)
		self.van.dock(self.bike5)
		self.van.dock(self.bike6)
		self.van.dock(self.bike7)
		self.van.dock(self.bike8)
		self.van.dock(self.bike9)
		self.van.dock(self.bike10)
		assert_equal(self.van.dock(self.bike11), "Cannot dock any more bikes")