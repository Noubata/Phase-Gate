import unittest
from game_quizz import guess

class TestGameQuizz (unittest.TestCase):

	def test_that_guess_collects_input(self):

		actual_input = guess(1)
		expected_answer = 1
		
		self.assertEqual(actual_input, expected_answer)

	def test_that_only_integer_is_accepted(self):

		try:
			actual_input = guess("hey")
			expected_answer = 1
		except:

			raise ValueError("Invalid input Oga!")