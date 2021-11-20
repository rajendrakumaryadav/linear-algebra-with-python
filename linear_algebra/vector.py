import math
from typing import List

Vector = List[float]


class Vector:
	"""
	__date__ = "19-11-2021"
	"""
	
	def __init__(self):
		print("Initializing Matrix...")
	
	def assert_length(self, v: Vector, w: Vector):
		assert len(w) == len(v), "Vector must be of same length"
	
	def addition(self, v: Vector, w: Vector) -> Vector:
		self.assert_length(v, w)
		return [v_i + w_i for v_i, w_i in zip(v, w)]
	
	def subtract(self, v: Vector, w: Vector) -> Vector:
		self.assert_length(v, w)
		return [v_i - w_i for v_i, w_i in zip(v, w)]
	
	def vector_sum(self, vectors: List[Vector]) -> Vector:
		assert vectors, "no vectors provided!"
		
		num_elements = len(vectors[0])
		assert all(len(v) == num_elements for v in vectors), "different sizes"
		
		return [
			sum(vector[i] for vector in vectors)
			for i in range(num_elements)
		]
	
	def scaler_multiply(self, c: float, v: Vector) -> Vector:
		"""multiply all elements of vector with c
		```python
			c*v_i
		```
		"""
		return [c * v_i for v_i in v]
	
	def vector_mean(self, vectors: List[Vector]) -> Vector:
		n = len(vectors)  # length of vectors
		# reusing scaler_multiply and vector_sum() previously defined.
		return self.scaler_multiply(1 / n, self.vector_sum(vectors))
	
	def dot(self, v: Vector, w: Vector) -> float:
		assert len(v) == len(w), "Vectors size mismatched."
		return sum(v_i * w_i for v_i, w_i in zip(v, w))
	
	def sum_of_square(self, v: Vector) -> float:
		return self.dot(v, v)  # reusing dot()
	
	def magnitude(self, v: Vector) -> float:
		return math.sqrt(self.sum_of_square(v))
	
	def squared_distance(self, v: Vector, w: Vector) -> float:
		return self.sum_of_square(self.subtract(v, w))
	
	def distance(self, v1: Vector, v2: Vector) -> float:
		return math.sqrt(self.squared_distance(v1, v2))
