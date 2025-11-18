#Find the first non-repeating character in a string


#solution 1:
def first_non_repeating_charachter(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return "No such character found"


#solution 2:
def first_non_repeating_character2(s):
    char_dic = {}
    for i in s:
        if i in char_dic:
            char_dic[i] += 1
        else:
            char_dic[i] = 1
           
    for i in s:
        if char_dic[i] == 1:
            return i
    return "No such character found"


         
        


s = "swiss"
result = first_non_repeating_character2(s)
print(f"The first non-repeating character in '{s}' is: {result}")