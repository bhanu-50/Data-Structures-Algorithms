#Count the frequency of each character in a string
def count_frq(s):
    dic = {}
    for i in range(len(s)):
        if s[i] in dic:
            dic[s[i]] += 1
        else:
            dic[s[i]] = 1
    return dic


s = "Safukgakfjhdafkjhdkfjgakfgdsfkjgdsfgdkjfg"
print(count_frq(s)) 
