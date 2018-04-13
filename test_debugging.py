# test_debugging.py
try:

    a = int(input("Enter a number: "))
    b = int(input("enter another number: "))
    print("a/b: ", a/b)


except ValueError:
    print("Could not convert to a number.")

except ZeroDivisionError:
    print("Can't divide by zero. ")
except:
    print("Bug in user input.")

