###### Intro to truthy and flasy values
# number = 0
# if number:
#     print("This will NOT print because 0 is falsy")

# number = -7
# if number:
#     print("This will print 7 because 7 is truthy")


##### Truthy Values
"""
# Non-empty sequences or collections
# Numeric values not equal to zero
# constant: True
"""

# if [1, 2]:
#     print("Non-empty list is truthy")

# if -4:
#     print("-4 is truthy")

##### Falsy values
"""
# empty sequences and collections
# number: 0 (integer), 0.0 (float), 0j (comples)
# constants: None, False
"""

# if not 0:
#     print("0 is falsy")
# if not []:
#     print("empty list is falsy")

####### even/odd number##############
num1 = 7
num2 = 4

# if num1 % 2:
#     print(num1, "is odd")
# else:
#     print(num1, "is even")

# if num2 % 2:
#     print(num2, "is odd")
# else:
#     print(num2, "is even")

######### Built-in bool() functions #####################

print(bool(7))
print(bool(0))
print(bool([1, 2, 3]))
print(bool([]))
print(bool(None))