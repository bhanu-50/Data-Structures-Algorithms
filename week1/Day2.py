#2) Reverse an array in place
def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    while left<right:
        temp = arr[left]             
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
    return arr

def reverse_array_recursive(arr, left, right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse_array_recursive(arr, left + 1, right - 1)

def reverse_arr(arr):
    return arr[::-1]



arr = [3,5,100,8,0,7]
reversed_arr = reverse_arr(arr)  
print("Reversed array:", reversed_arr)

