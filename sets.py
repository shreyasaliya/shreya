s = set()
# print(type(s))
l=[1, 2, 3, 4]
s_from_list = set([1, 2, 3, 4])  #You can write this also  s_from_list = set(l)
print(s_from_list)
print(type(s_from_list))


s.add(1)
s.add(1)
s.add(2)
s.add(3)
s.remove(3)
s1 = s.union({1,2,3,4})
s2 = s.intersection({1,2,3,4})
print(s, s1, s2)


print(len(s))
print(min(s))
print(max(s))
s3 = {4,6}
print(s.isdisjoint(s3))

