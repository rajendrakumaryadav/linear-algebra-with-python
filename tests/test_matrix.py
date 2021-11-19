import unittest
from linear_algebra import matrix


class MyTestCase(unittest.TestCase):
	mat_obj = matrix.Matrix()
	v1 = [1, 2, 3]
	v2 = [4, 5, 6]
	
	def test_vector_addition(self):
		assert self.mat_obj.add_vector(self.v1, self.v2) == [5, 7, 9]
		self.assertEqual(self.mat_obj.add_vector(self.v1, self.v2), [5, 7, 9])


if __name__ == '__main__':
	unittest.main()
