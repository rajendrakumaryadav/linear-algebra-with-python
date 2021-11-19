import unittest
from typing import List

from linear_algebra import matrix


class MyTestCase(unittest.TestCase):
	mat_obj = matrix.Matrix()
	v1: List[float] = [1, 2, 3]
	v2: List[float] = [4, 5, 6]
	vec_add: List[float] = [5, 7, 9]
	vec_sub: List[float] = [-3, -3, -3]
	
	def test_addition(self):
		assert self.mat_obj.addition(self.v1, self.v2) == self.vec_add
		self.assertEqual(self.mat_obj.addition(self.v1, self.v2), self.vec_add)
	
	def test_subtract(self):
		assert self.mat_obj.subtract(self.v1, self.v2) == self.vec_sub
		self.assertEqual(self.mat_obj.subtract(self.v1, self.v2), self.vec_sub)
	
	def test_vector_sums(self):
		assert self.mat_obj.vector_sum([self.v1, self.v2]) == self.vec_add
		self.assertEqual(self.mat_obj.vector_sum([self.v1, self.v2]), self.vec_add)
	
	if __name__ == '__main__':
		unittest.main()
