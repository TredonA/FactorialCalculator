# Factorial Calculator | By Tredon Austin
# Project to help nail the concept of recursion through python
# implementation. One factorial function will be done through loops. The other
# will be done through recursion.

def factorialLoop(num):
    factorial = 1
    numIndex = num
    if num == 0:
        return 1
    while numIndex != 0:
        factorial *= numIndex
        numIndex -= 1
    return factorial

def factorialRecursion(num):
    if num == 0:
        return 1
    return num * factorialRecursion(num - 1)

userNum = input("Please enter a number that you would like to calculate the" +
      " factorial of: ")
while not userNum.isdigit():
    userNum = input("Value entered in is not a valid number."
                    + " Please try again: ")
print("Value from the factorial function implemented by loop: " +
      str(factorialLoop(int(userNum))))
print("Value from the factorial function implemented by recursion: " + 
      str(factorialRecursion(int(userNum))))

# Another comment to practice Visual Studio Pushing