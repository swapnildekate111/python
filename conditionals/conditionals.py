############### if-else statement
# name = input("What's you name? ")
# age = int(input("What's your age? "))

# if (age >= 18):
#     print(f'congratulations {name} you can cast your vote')
# else:
#     print(f"Sorry {name} you can't cast your vote")

# print("eligible") if age >= 18 else print("not eligible")

################## if else if else ladder

# num = int(input("Enter number: "))

# if num > 0:
#     print("positive")
# elif num < 0:
#     print("negative")
# else:
#     print("zero")

# age = int(input("Enter you age: "))

# if age <= 12:
#     print("child")
# elif age <= 19:
#     print("Teenager")
# elif age <= 35:
#     print("young adult")
# else:
#     print("Adult")

################### Nested if-else statement

# is_member = bool(input("Are you memeber? "))

# if age >= 60:
#     if is_member:
#         print("30% Senior dicount")
#     else:
#         print("20% Senior discount")
# else:
#     print("Not eligible for Senior discount")

# if age >= 60 and is_member:
#     print("30% Senior dicount")
# elif age >= 60 and not is_member:
#     print("20% Senior discount")
# else:
#     print("Not eligible for Senior discount")

########################  Ternary Operation

# citizen = "Adult" if age >= 18 else "Minor"
# print(citizen)

######################## Match-case statement

day = int(input("Enter day number: "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednessday")
    case 4:
        print('Thursday')
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Day!!!")