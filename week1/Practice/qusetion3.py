#Remove duplicate elements from an array without using a set

def rem_dupl(arr):
    new_arr = []
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    return new_arr


arr = [1,1,2,3,4,4,5,5,4,5,6,7,8,8,6,9]
print(rem_dupl(arr))