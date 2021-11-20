import unittest
from typing import List

from linear_algebra import matrix

Matrix = List[List[float]]


class TestMatrix(unittest.TestCase):
	mat_obj = matrix.Matrix()
	a: Matrix = [[1, 2, 3], [2, 3, 4]]
	
	def test_shape(self):
		self.assertEqual(self.mat_obj.shape(self.a), (2, 3))


if __name__ == '__main__':
	unittest.main()
