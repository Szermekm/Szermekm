# Write a program that reads a number form the standard input,
# If the number is zero or smaller it should print: Not enough
# If the number is one it should print: One
# If the number is two it should print: Two
# If the number is more than two it should print: A lot

user_input_1 = int(input())
if user_input_1 == 0:
    print("Not enough")
elif user_input_1 == 1:
    print("One")
elif user_input_1 == 2:
    print("Two")
else:
    print("A lot")
