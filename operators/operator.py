############################### OPERATORS ###############################
"""
# Arithmetic Operator (+, -, *, /, %) [x]
# Relational Operator (<, >, <=, >=, !=, ==) [x]
# Logical Operator (AND, OR, NOT) [x]
# Bitwise Operator (&, |, ^, ~, <<, >>) [x]
# Assignment Operator (=, +=, -=, *=, /=) [x]
# Ternary Operator (x if condition else y)
# Identity Operator (is, is not) [X]
"""

############# Arithmetic Operator #############
a = 15
b = 4

# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b) # returns floating(datatype) point value
# print("Floor Division:", a // b) # returns integer(datatype) value
# print("Modulo:", a % b)
# print("Exponentiation:", a ** b)

############# Relational Operator #############
a = 13
b = 33

# print(a > b) # 13 is greater than 33 -> False
# print(a < b) # 13 is less than 33 -> True
# print(a == b) # 13 is equal to 33 -> False
# print(a != b) # 13 is not equal to 33 -> True
# print(a >= b) # 13 is greater than or equal to 33 -> False
# print(a <= b) # 13 is less than or equal to 33 -> True

############# Logical Operator #############
a = True
b = False

# print(a and b) ## False
# print(a or b) # True
# print(not b) # True

############# Bitwise Operator #############
a = 10
b = 4

# print(a & b)
# print(a | b)
# print(~a)
# print(a ^ b)
# print(a >> 2)
# print(a << 2)


############# Assignment Operator #############
a = 10
b = a

# print(b)

# b += a # b = b + a
# print(b)

# b -= a # b = b - a
# print(b)

# b *= a # b = b * a
# print(b)

# b /= a # b = b / a
# print(a)

############# Identity Operator #############

"""
# is     -> True if the operands are identical
# is not -> True if the operands are not identical
"""

a = int(10)
b = 20
c = int("001010", 2)

# print (a is not b)
# print (a is c)

############# Membership Operator ############
"""
# in            -> True if value is found in sequence
# not in        -> True if value is not found in sequence
"""

x = 24
y = 20

ls = [10, 20, 30, 40, 50]

# if x not in ls:
#     print("x is NOT present in given list")
# else:
#     print("x is present in given list")

# if y not in ls:
#     print("y not in list")
# else:
#     print("y is in list")

############# Ternary Operator ############

# a = int(input("Number a: "))
# b = int(input("Number b: "))

min = a if a < b else b # Ternary operator

# print("Mininum:", min)

############# Precedence and Associativity of Operators ############
# PEMDAS rule
expr = 10 + 20 * 30
# print(expr)

name = 'Alex'
age = 0

if name == "Alex" or name == 'John' and age >= 2:
    print("Hello!")
else:
    print("Goodbye!!!")

############# Operator Associativity ###############
print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)