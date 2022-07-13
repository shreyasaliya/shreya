import random
from secrets import choice

random_number = random.randint(0,1)
print(random_number)
rand = random.random() *100
print(rand)
list = ["shreya", "aesvi", "kajal", "priti"]
choice = random.choice(list)
print(choice)