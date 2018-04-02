# branching_iteration.py

# name = "tsofa"
# greeting = "hi " + name
# print(greeting)

# #text = raw_input("type anything please")
# text = str(input("type anything please"))
# print(5*text)

# if true prog ends and doesn't look at other conditions.
x = float(input("Enter a value for x: "))
y = float(input("Enter value for y: "))

if x == y :
    print("x and y are equal.")
    if y != 0:
        print("therefore, x / y is ", x/y)

elif x < y:
    print("x is smaller")

else:
    print("y is smaller")

print("Thanks")
