# i =0

# while (True):
#     if i+1<5:
#         i =i+1
#         continue

#     print(i+1, end=" ")
#     if(i ==44):
#         i =i+1
#         break  #stop the loop
#     i = i+1


   
while (True):
    n1 = int(input("enter a number: \n"))
    if n1>100:
        print("your number is greater than 100\n")
        break
    else:
        print("try again\n")
        continue