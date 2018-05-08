a = 'myname'
print(a.index('m'))
b = [1,3,5]
# print(b.find(1))
# print(b.add(1))
print('%.2e' % 2**5)

def strReverse(str0):
    if len(str0) == 0:
        return str0
    else:
        return str0[-1] + strReverse(str0[:-1])

print(strReverse('apple'))

def isPal(s): # check if s is a palindrome
    if len(s) <= 1:
        return True
    else:
        return s[0].lower() == s[-1].lower() and isPal(s[1:-1])

def removeWhite(s): # remove blanks / symbols
    if len(s) == 0:
        return s
    else:
        if ord(s[0].lower()) in range(ord('a'), ord('z') + 1):
            return s[0] + removeWhite(s[1:])
        else:
            return removeWhite(s[1:])

print(removeWhite("Madam i'm adam"))
print(isPal(removeWhite("madam i'm adam")))

a = 'Lower!'
print(a[0].lower())
