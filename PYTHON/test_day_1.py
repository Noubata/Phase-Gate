import unittest
from day_1 import day_1

class Test_day_1(unittest.TestCase):

	def test_that_it_only_accepts_integer(self):

		actual = day_1(1)
		expected = 1

		self.assertEquals(actual, expected)
	
	def test_that_it_raises_error_when_entered_other_than_integer(self):

		try:
			actual = day_1(1)
		except:

			raise ValueError("Invalid input!")