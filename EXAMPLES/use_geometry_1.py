import sys
import alpha.mathlib.geometry as geometry # find geometry.py and run the code
from alpha.mathlib import geometry

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)
print(f"{geometry.PI = }")

# module/package search algorithm
# 1. current folder
# 2. folders in PYTHONPATH
# 3. folders in install folder + "lib"  (sys.prefix)

print(f"{sys.prefix = }")
print(f"{sys.executable = }")
print()
for path in sys.path:
    print(path)
print()