import unittest
from parking_system import my_parking

class TestParkingSystem(unittest.TestCase):

	def test_that_a_parking_exists(self):

		actual = my_parking()

		expected = {'Space 1' : None, 'Space 2' : 6, 'Space 3' : None, 'Space 4' : None, 'Space 5' : None, 'Space 6' : None, 'Space 7' : None, 'Space 8' : None, 'Space 9' : None, 'Space 10' : None, 'Space 11' : None, 'Space 12' : None, 'Space 13' : None, 'Space 14' : None, 'Space 15' : None, 'Space 16' : None, 'Space 17' : None, 'Space 18' : None, 'Space 19' : None, 'Space 20' : None}

		self.assertEqual(actual, expected)

	def test_that_the_parking_is_either_occupied_or_not(self):

		actual = my_parking()
		expected =  {'Space 1' : None, 'Space 2' : 6, 'Space 3' : None, 'Space 4' : None, 'Space 5' : None, 'Space 6' : None, 'Space 7' : None, 'Space 8' : None, 'Space 9' : None, 'Space 10' : None, 'Space 11' : None, 'Space 12' : None, 'Space 13' : None, 'Space 14' : None, 'Space 15' : None, 'Space 16' : None, 'Space 17' : None, 'Space 18' : None, 'Space 19' : None, 'Space 20' : None}
