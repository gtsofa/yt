# branching_iteration.py

# name = "tsofa"
# greeting = "hi " + name
# print(greeting)

# #text = raw_input("type anything please")
# text = str(input("type anything please"))
# print(5*text)

# # if true prog ends and doesn't look at other conditions.
# x = float(input("Enter a value for x: "))
# y = float(input("Enter value for y: "))

# if x == y :
#     print("x and y are equal.")
#     if y != 0:
#         print("therefore, x / y is ", x/y)

# elif x < y:
#     print("x is smaller")

# else:
#     print("y is smaller")

# print("Thanks")

# n = raw_input("You're in the lost forest. Go right or left? ")

# while n == "right":
#     n = raw_input("You're in the lost forest. Go right or left? ")

# print("Yaay. You got out of the lost forest. ")

# for loops
# syntax : 
'''
for <varibale> in range(<some number):
    expression
    expression
    ...

--> each time through the loop, <variable> takes a value
--> first tiem, <varialbe> starts at the smallest value
--> next time , <variable> gets the prev value + 1 
--> etc
--> range(start, stop, step)
--> default values are start = 0 and step = 1 and optional
--> loop until value is stop - 1
'''
# for loop examples
# mysum = 0
# for i in range(5, 7):
#     mysum += i

# print(mysum) # 11

mysum = 0
for i in range(5, 7):
    mysum += i

print(mysum)
