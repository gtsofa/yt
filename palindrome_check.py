# palindrome_check.py

# recursion in strings 

def isPalindrome(s):
    # check if string is a palindrome
    def toChars(s):
        # convert string to characters
        s = s.lower()

        ans = ''

        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxy':
                ans = ans + c 
        return ans

    def isPal(s):
        #Return true/false if string is a palindrome
        if len(s) <= 1:
            return True 
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))

# test goes here:
test1 = isPalindrome('ama')
print(test1)
