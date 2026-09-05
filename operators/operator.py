############################### OPERATORS ###############################
"""
# Arithmetic Operator (+, -, *, /, %) [x]
# Relational Operator (<, >, <=, >=, !=, ==) [x]
# Logical Operator (AND, OR, NOT) [x]
# Bitwise Operator (&, |, ^, ~, <<, >>) [x]
# Assignment Operator (=, +=, -=, *=, /=)
# Ternary Operator (x if condition else y)
# Identity Operator (is, is not)
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

print(b)

b += a # b = b + a
print(b)

b -= a # b = b - a
print(b)

b *= a # b = b * a
print(b)

b /= a # b = b / a
print(a)