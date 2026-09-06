""" Syntax
variale := expression
"""

#################### Example 1: walrus operator in while loop
# num = [1, 2, 3, 4]

# while (n := len(num)) > 0:
#     print(num.pop())

# print(len(num))

#################### Example 2: Comparing with and without walrus operator
d = [
    {"userid": 1, "name": "Rahul", "completed": False},
    {"userid": 1, "name": "Rohit", "completed": False},
    {"userid": 1, "name": "Ram", "completed": False},
    {"userid": 1, "name": "Rachit", "completed": True},
]

# print("With walrus operator:")
# for entry in d:
#     if name := entry.get("name"):
#         print(name)

# print("Without walrus operator:")
# for entery in d:
#     name = entry.get("name")
#     if name:
#         print(name)

#################### Example 3: Simplifying user input loops

foods = []
print(foods)

while (food := input("what food you you like? (type 'quit' to stop): ")) != 'quit':
    foods.append(food)

print(foods)