with open("shreya.txt") as f:
    a = f.readlines()
    print(a)


f = open("shreya.txt")
print(f.readlines())
print(f.readline())
f.close()