# string_manipulation.py

a = "abcdefgh"
print(a[::-1])# it's like reverse method.

# for loop with loop variable var
for var in range(4,6):
    print(var)

#looping through a string
s = "abcdefgh"
for index in range(len(s)):
    if s[index] == "i" or s[index] == "u":
        print("There is an i or u ")
# code above is same as below
for char in s:
    if char == "i" or char == "u":
        print("Thre is an i or u")
