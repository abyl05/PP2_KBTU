q, w, e = 133, 642, 192
a, s, d = 200, 324, 7235
if q > a:
  print("q is greater than a")
elif w > s:
  print("w is greater than s")
elif e > d:
  print("e is greater than d")
else:
  print("Error")
if q < a:
  print("q is less than a")
elif w < s:
  print("w is less than s")
elif e < d:
  print("e is less than d")
else:
  print("Error")
if q == a:
  print("q is equal than a")
elif w == s:
  print("w is equal than s")
elif e == d:
  print("e is equal than d")
else:
  print("Error")
if q != a:
  print("q is not equal than a")
elif w != s:
  print("w is not equal than s")
elif e != d:
  print("e is not equal than d")
else:
  print("Error")
if q >= a:
  print("q is greater or equal than a")
elif w >= s:
  print("w is greater or equal than s")
elif e >= d:
  print("e is greater or equal than d")
else:
  print("Error")
if q <= a:
  print("q is less or equal than a")
elif w <= s:
  print("w is less or equal than s")
elif e <= d:
  print("e is less or equal than d")
else:
  print("Error")

z, x, c, v = 1, 2, 3, 4
if z>x and c<v: print("Both conditions are True")
elif z<x and c>v: print("Both conditions are True")
elif z<x and c<v: print("Both conditions are True")
elif z>x and c>v: print("Both conditions are True")
if z>x or c<v: print("At least one of the conditions is True")
elif z<x or c>v: print("At least one of the conditions is True")
elif z>x or c>v: print("At least one of the conditions is True")
elif z<x or c<v: print("At least one of the conditions is True")
if not z>x: print("z is NOT greater than x")
elif not z>c: print("z is NOT greater than c")
elif not v>x: print("v is NOT greater than x")
elif not c>v: print("c is NOT greater than v")

if z > x:
  pass
if c != v:
  pass
if z == c:
  pass
if x < v:
  pass
if z >= v:
  pass