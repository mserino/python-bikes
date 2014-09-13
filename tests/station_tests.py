from nose.tools import *
import nose
from station.station import Station
from bike.bike import Bike

class TestStation(object):

	@classmethod
	def setup_class(klass):
		"""This method is run once for each class before any tests are run"""

	@classmethod
	def teardown_class(klass):
		"""This method is run once for each class _after_ all tests are run"""

	def setUp(self):
		"""This method is run once before _each_ test method is executed"""
		self.station = Station()
		self.bike = Bike()
		self.bike2 = Bike()
		self.bike3 = Bike()
		self.bike4 = Bike()
		self.bike5 = Bike()
		self.bike6 = Bike()

	def teardown(self):
		"""This method is run once after _each_ test method is executed"""
		pass

	def test_station_can_dock_maximum_five_bikes(self):
		assert_equal(self.station.capacity, 5)

	def test_station_is_not_full(self):
		self.station.dock(self.bike)
		self.station.dock(self.bike2)
		assert_equal(self.station.is_full(), "not full")

	def test_station_can_be_full(self):
		self.station.dock(self.bike)
		self.station.dock(self.bike2)
		self.station.dock(self.bike3)
		self.station.dock(self.bike4)
		self.station.dock(self.bike5)
		assert_equal(self.station.is_full(), "full")

	def test_station_cannot_dock_more_than_five_bikes(self):
		self.station.dock(self.bike)
		self.station.dock(self.bike2)
		self.station.dock(self.bike3)
		self.station.dock(self.bike4)
		self.station.dock(self.bike5)
		assert_equal(self.station.dock(self.bike6), "Cannot dock any more bikes")