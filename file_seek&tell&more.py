f = open("shreya.txt")
f.seek(11)
print(f.tell())   #file pointer location
print(f.readline())
# print(f.tell())
# f.seek(10)
f.seek(0)
print(f.readline())
# print(f.tell())
f.close()