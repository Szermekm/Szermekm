# - Create a variable named `firstArrayOfNumbers`
#   with the following content: `[1, 2, 3]`
# - Create a variable named `secondArrayOfNumbers`
#   with the following content: `[4, 5]`
# - Print "secondArrayOfNumbers is longer" if `secondArrayOfNumbers` has more
#   elements than `firstArrayOfNumbers`

firstArrayOfNumbers = [1, 2, 3]
secondArrayOfNumbers = [4, 5]
#if "secondArrayOfNumbers" "firstArrayOfNumbers"
 #   print("secondArrayOfNumbers is longer")

a = len(firstArrayOfNumbers)
b = len(secondArrayOfNumbers)
if b > a:
    print("secondArrayOfNumbers is longer")
