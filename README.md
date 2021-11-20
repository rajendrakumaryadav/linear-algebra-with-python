### Linear Algebra

#### Fork to do more improvement or clone to learn interactively

```bash
$ git clone https://github.com/rajendrakumaryadav/linear-algebra-with-python.git
$ cd linear-algebra-with-python/

```

* if you wish to use this package please follow

```python
from linear_algebra import vector

mat_obj = vector.Vector()
assert mat_obj.subtract([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
```

* To Test code run run_all_test.sh

```bash
$ bash ./run_all_test.sh
==================================================== test session starts ====================================================
platform linux -- Python 3.8.12, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /home/username/Documents/linear-algebra
collected 9 items                                                                                                           

tests/test_matrix.py .                                                                                                [ 11%]
tests/test_vector.py ........                                                                                         [100%]

===================================================== 9 passed in 0.11s =====================================================
```

---
### Credit
- All the code is based on the [`Data Science from Scratch`](https://www.oreilly.com/library/view/data-science-from/9781491901410/) authored by __Joel Grus__, ISBN: **9781491901427**.
- Published by: O'Reilly Media, Inc.

