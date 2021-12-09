# define a function to check if the entered number is actually a number
def checkValidity (message):
    while True:
        value = input (message)
        try:
            val = int(value)
            break
        except ValueError:
            try:
                val = float(value)
                break
            except ValueError:
                print("The entered value is not a number!, Try again!")
    return val

# take the 2 inputs
firstValue = checkValidity("First Number: ")
secondValue = checkValidity("Second number: ")   

# check if the operation inputted is an available operation in this simple calculator
# and return the result of the operation
while True:  
    op = input ("Operation: ")
    if (op == "+"):
        result = firstValue+secondValue
        break
    elif (op == "-"):
        result = firstValue-secondValue
        break
    elif (op == "/"):
        if (secondValue == 0):
            result = "D.N.E"
            break
        result = firstValue/secondValue
        break
    elif (op == "*"):
        result = firstValue*secondValue
        break
    else:
        print("This is not an available operation! Try again!")   


# print the result of the operation done by this calculator
print ("The result =", result)


# This simple calculator is made by Mohamed Gamal