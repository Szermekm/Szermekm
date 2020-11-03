# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

n=int(input())
for i in range(n):
    X = 1
    for j in range(n-1-i): # -1 to reduce by factor of 10
        X = (X*10)+1
    print(X)