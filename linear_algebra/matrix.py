from typing import List
from typing import Tuple

from linear_algebra.vector import Vector

Matrix = List[List[float]]


class Matrix:
	def __init__(self):
		vector = Vector()
		pass
	
	def shape(self, a: Matrix) -> Tuple[int, int]:
		num_rows = len(a)
		num_cols = len(a[0]) if a else 0
		return num_rows, num_cols
	