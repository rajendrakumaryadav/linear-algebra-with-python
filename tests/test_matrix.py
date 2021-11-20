import unittest
from typing import List

from linear_algebra import matrix


class MyTestCase(unittest.TestCase):
	mat_obj = matrix.Matrix()
	Vector = matrix.Vector
	v1: List[float] = [1, 2, 3]
	v2: List[float] = [4, 5, 6]
	vec_add: List[float] = [5, 7, 9]
	vec_sub: List[float] = [-3, -3, -3]
	
	# def draw(self, v1: Vector, v2: Vector, result: Vector):
	# 	plt.plot(v1, v2, result)
	# 	plt.show()
	
	def test_addition(self):
		assert self.mat_obj.addition(self.v1, self.v2) == self.vec_add
		# self.draw(self.v1, self.v2, result=self.mat_obj.addition(self.v1, self.v2))
		self.assertEqual(self.mat_obj.addition(self.v1, self.v2), self.vec_add)
	
	def test_subtract(self):
		assert self.mat_obj.subtract(self.v1, self.v2) == self.vec_sub
		self.assertEqual(self.mat_obj.subtract(self.v1, self.v2), self.vec_sub)
	
	def test_vector_sums(self):
		assert self.mat_obj.vector_sum([self.v1, self.v2]) == self.vec_add
		self.assertEqual(self.mat_obj.vector_sum([self.v1, self.v2]), self.vec_add)
	
	def test_scaler_multiply(self):
		v1 = [3, 6, 9]
		assert self.mat_obj.scaler_multiply(1 / 3, v1) == [1, 2, 3]
		self.assertEqual(self.mat_obj.scaler_multiply(1 / 3, v1), [1, 2, 3])
	
	def test_vectors_mean(self):
		assert self.mat_obj.vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]
		self.assertEqual(self.mat_obj.vector_mean([[1, 2], [3, 4], [5, 6]]), [3, 4])
	
	def test_vector_dot_products(self):
		self.assertEqual(self.mat_obj.dot(self.v1, self.v2), 32)
	
	def test_sum_of_square(self):
		self.assertEqual(self.mat_obj.sum_of_square(self.v1), 14)
		
		# def test_vector_dot_product_false(self):
		# 	self.assertFalse(self.mat_obj.dot(self.v1, self.v2), 32)
		
		if __name__ == '__main__':
			unittest.main()
