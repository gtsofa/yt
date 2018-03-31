# a smart calculator where the use presses even the operators

# Enter calculations : 5 * 6 
# 5 * 6 = 30
# Store the user input of the two numbers and the operator
#num1, operator, num2 = input("Enter Calculation:")
#num1, num2 = input("enter numbers:").split()
num1, operator, num2 = raw_input("Enter two numbers and the other operate in between:").split()
# Convert the strings into integers
num1 = int(num1)
num2 = int(num2)

#print("{} {}".format(num1, num2))


#if + then we need to provide output based on addition
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))

elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1-num2))

elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1*num2))

elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1/num2))

else:
    print("use either + - * or / next time.")
# # print the result
