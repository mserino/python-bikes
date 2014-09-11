import unittest
from person import Person 

class PersonTest(unittest.TestCase):

	def setUp(self):
		self.person = Person()

if __name__ == '__main__':
	unittest.main()