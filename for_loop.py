list = [ ["shreya", 2], ["kajal", 5], ["priti",45], ["aesvi",250] ]
list1 = ("shreya", "kajal", "priti", "aesvi")

dict1 =  dict(list)
print(dict1)

# print(list[0], list[1], list[2], list[3])

# tuple
for item in list1:
    print(item)

# list
for item,lollypop in list:
    print(item, "and lollypop is:",lollypop)

# dictionary
for item,lollypop in dict1.items():
    print(item, "and lollypop is:",lollypop)

# key from dictionary
for item in dict1:
    print(item)



items = [int, float, "shreya", 5, 3, 76, 450, 563267]

for item in items:
    if str(item).isnumeric() and item>6:
        print(item)