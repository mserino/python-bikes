from nose.tools import *
import nose
from bike import Bike

class TestBike(object):

	@classmethod
	def setup_class(klass):
		"""This method is run once for each class before any tests are run"""

	@classmethod
	def teardown_class(klass):
		"""This method is run once for each class _after_ all tests are run"""

	def setUp(self):
		"""This method is run once before _each_ test method is executed"""
		self.bike = Bike()

	def teardown(self):
		"""This method is run once after _each_ test method is executed"""
		pass

	def test_bike_not_broken(self):
		assert_false(self.bike.broken)

	def test_bike_can_be_broken(self):
		self.bike.break_bike()
		assert_true(self.bike.broken)

	def test_bike_can_be_fixed(self):
		self.bike.break_bike()
		self.bike.fix_bike()
		assert_false(self.bike.broken)

	def test_fixed_status_of_the_bike_when_created(self):
		assert_equal(self.bike.status, "fixed")

	def test_broken_status_of_the_bike_when_broken(self):
		self.bike.break_bike()
		assert_equal(self.bike.status, "broken")

	def test_fixed_status_of_the_bike_when_fixed(self):
		self.bike.break_bike()
		self.bike.fix_bike()
		assert_equal(self.bike.status, "fixed")

if __name__ == '__main__':
	unittest.main()