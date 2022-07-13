print("How many rows you want to print")
n = int(input())
print("enter 1 or 0")
m = int(input())
new = bool(m)

if new == True:
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print()

elif new == False:
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print()

