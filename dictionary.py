# Dictionary is nothing but key value pairs 
d1 = {}
print(type(d1))
d2 = {"shreya":"burger", "kajal":"pizza", "aesvi":"Roti", "priti": {"B":"maggie", "L":"roti", "D":"chinese"}}
print(d2)
print(d2["shreya"])
print(d2["priti"])
print(d2["priti"]["B"])
d2["janvi"] = "junk food"
d2[420] = "pani puri"
print(d2)
del d2[420]
print(d2)

# d3 = d2.copy() #for not do changes in d2 copy is used
# del d3["shreya"]
# print(d2)

# print(d2.get("kajal"))
# d2.update({"leena":"toffee"})
# print(d2)
# print(d2.keys())
# print(d2.items())