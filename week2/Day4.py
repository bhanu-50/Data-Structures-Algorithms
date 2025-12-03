#Check for balanced parentheses using a stack.
def check_exp(s):
    dic = {'}':'{',')':'(',']':'['}
    stack = []
    for i in s:
        if i not in dic.keys():
            stack.append(i)
        else:
            if dic[i]==stack[-1]:
                stack.pop()
            else:
                return "Invalid Expression "
    
    return "Valid Expression"  
            

s = "[({)]"
print(check_exp(s))
x = "{({[]})}"
print(check_exp(x))