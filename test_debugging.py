# test_debugging.py
try:

    a = int(input("Enter a number: "))
    b = int(input("enter another number: "))
    print(a/b)

except:
    print("Bug in user input.")

