import unittest
from divide.divide_by_ten import divide_by_ten 

class TestDivideByThen(unittest.TestCase):

	def test_divide_by_ten(self):
		self.assertEqual(divide_by_ten(12), 4)

unittest.main()