#Find the second largest element in an array
#solution 1:
def second_larg(arr):
    arr.sort()
    return arr[-2]

#soluion 2:
def second_larg2(arr):
    larg = arr[0]
    sec_larg = arr[0]
    for i in arr[1:]:
        if i>larg:
           sec_larg = larg
           larg = i
        elif larg>i>sec_larg:
            sec_larg = i
    return sec_larg
        
    
arr = [3,1,6,2,9,12,7,10,14]
print(second_larg2(arr))