f = open("shreya2.txt", "w") 
a = f.write("shreya is good girl\n")
print(a)
f.close()


f = open("shreya2.txt", "a")  #for append write a instead of w
a = f.write("shreya is pretty girl\n")
print(a)
f.close()


# Handle read and write both
f=open("shreya3.txt", "r+")
print(f.read())
f.write("\nthank you!!")