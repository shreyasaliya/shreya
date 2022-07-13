def function_name_print(a, b, c, d):
    print(a, b, c, d)

function_name_print("shreya", "aesvi", "kajal", "priti")
# not possible to pass 5 arguments
# function_name_print["shreya", "aesvi", "kajal", "priti", "ravina"]

def funargs(normal, *argskajal, **kwargsbala):
    print(normal)
    for item in argskajal:
        print(item)
    print("\nthis is our heroes")
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")

shreya = ["kajal", "aesvi", "shreya"]
normal = "This is normal argument"
kw = {"shreya":"A", "kajal":"B", "aesvi":"C"}
funargs(normal, *shreya, **kw)