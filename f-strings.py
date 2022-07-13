import math

me ="Shreya"
t1 = 6
a = "this is %s"%me
print(a)
b = "this is %s %s"%(me,t1)
print(b)
c ="this is {1} {0}"
d = c.format(me, t1)
print(d)

# f strings
z = f"This is {me} {t1} {4*26} {math.cos(65)}"
print(z)
