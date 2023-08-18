s = {'a','b','c','d'}

s.add('e')
print(s)

s.discard('b')
print(s)

s.remove('c')
print(s)


s.pop()
print(s)


s.clear()
print(s)


s1 = {1,2,3}
s2 = {2,3,4}


print(s1.intersection(s2))


print(s1.union(s2))

print(s1.symmetric_difference(s2))

s1.update(s2)
print(s2)
l1 = [1,2,3,4]
s1 = set(l1)
print(s1)


