print("enter first number:")
var1 = int(input())
print("enter second number")
var2 = int(input())
print("enter operator which you want to perfome +,-,*,/")
var3 = input()

if var3 == "+":
    if var1 == 56 and var2 == 9:
        print("your result is:77")
    else:
        print("your result is:",var1+var2)
elif var3 == "-":
    print("your result is:",var1-var2)
elif var3 == "*":
    if var1 == 45 and var2 ==3:
        print("your result is:555")
    else:
        print("your result is:",var1*var2)
elif var3 == "/":
    if var1 == 56 and var2 == 6:
        print("your result is:4")
    else:
        print("your result is:",var1/var2)


