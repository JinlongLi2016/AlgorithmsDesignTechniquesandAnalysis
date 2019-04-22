import unittest
from sample_codes import *

class MyTest(unittest.TestCase):
	def testsquare_function(self):
		self.assertEqual(permutations1(3), 4)

if __name__ == '__main__':
	unittest.main()