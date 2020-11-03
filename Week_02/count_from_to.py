# Create a program that asks for two numbers
# If the second number is not bigger than the first one it should print:
# "The second number should be bigger"
#
# If it is bigger it should count from the first number to the second by one
#
# example:
#
# first number: 3, second number: 6, should print:
#
# 3
# 4
# 5

a = int(input())
b = int(input())

if b <= a:
    print("The second number should be bigger")
elif b > a:
    for x in range(a,b,1):
        print(x)