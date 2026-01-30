a = " Rome wasn’t ,built in a day. "
b = " Actions speak, louder than words. "
c = " It’s no use ,crying over spilled milk. "
d = " Still waters, run deep. "
e = " Curiosity, killed the cat. "

print(a.upper(), a.lower(), a.strip(), a.replace('a', 'b'), a.split(","))
print(b.upper(), b.lower(), b.strip(), b.replace('a', 'b'), b.split(","))
print(c.upper(), c.lower(), c.strip(), c.replace('a', 'b'), c.split(","))
print(d.upper(), d.lower(), d.strip(), d.replace('a', 'b'), d.split(","))
print(e.upper(), e.lower(), e.strip(), e.replace('a', 'b'), e.split(","))

q = a + b
print(q)
w = b + c
print(w)
r = c + d
print(r)
t = d + e
print(t)
y = e + a
print(y)

q1 = a + " " + b
print(q1)
w1 = b + " " + c
print(w1)
r1 = c + " " + d
print(r1)
t1 = d + " " + e
print(t1)
y1 = e + " " + a
print(y1)