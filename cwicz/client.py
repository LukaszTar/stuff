import mathlib
try:
	mathlib.func()
except mathlib.NumErr as x:
	print(x.__class__)
