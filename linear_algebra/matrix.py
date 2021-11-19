from typing import List

Vector = List[float]


class Matrix:
	"""
	__date__ = "19-11-2021"
	"""
	
	def __init__(self):
		pass
	
	def add_vector(self, v: Vector, w: Vector) -> Vector:
		assert len(v) == len(w), "Vector must be of same length"
		return [v_i + w_i for v_i, w_i in zip(v, w)]
