# 4) Given a string, check if it’s a palindrome

#solution 1: using slicing
def is_palindrome1(s):
    return "Yes" if s==s[::-1] else "No"


#solution 2: using two pointers
def is_palindrome2(s):
    left,right = 0,len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return "No"
        left+=1
        right-=1
    return "Yes"

#Solution 3: for number palindrome
def num_palindrome(num):
    original = num
    rev=0
    while num>0:
        rem = num%10
        rev = rev*10 + rem
        num=num//10
    return "Yes" if rev==original else "No"




string = 10001
result = num_palindrome(string)
print(f'Is the string "{string}" a palindrome? {result}')
