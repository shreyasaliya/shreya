# import readline


# open() 
# read()
# readline()
# readlines()

f = open("shreya.txt")
# content = f.read(10)                 
# print(content)

# print(f.readlines())

# print(f.readline())
# print(f.readline())
# print(f.readline())

# for line in f:
# 	print(line, end="")

content = f.read(34455)
print("1", content)

content = f.read(34455)
print("2", content)

f.close()

