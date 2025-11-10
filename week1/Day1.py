#1) Find the largest and smallest elements in an array

def find_lrg_and_sml1(arr):
    arr.sort()
    min_val, max_val = arr[0],arr[-1]
    return min_val, max_val

def find_lrg_and_sml2(arr):
    min_val = arr[0]
    max_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
        
    return min_val, max_val

arr = [3,5,100,8,0,7]
min_val, max_val = find_lrg_and_sml2(arr)
print("Smallest element:", min_val)
print("Largest element:", max_val)