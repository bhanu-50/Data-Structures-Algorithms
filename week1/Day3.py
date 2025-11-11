#3) Move all zeros to the end without changing the order of non-zero element

#solution 1:
def move_zeros_to_end1(arr):
    non_zero_elements = [num for num in arr if num!=0]
    zero_count = arr.count(0)

    return non_zero_elements + [0]*zero_count


#solution 2:
def move_zeros_to_end2(arr):
    non_zero_index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index],arr[i] = arr[i],arr[non_zero_index]
            non_zero_index += 1
    return arr

arr = [0,1,0,3,12]
result = move_zeros_to_end2(arr)
print(result)  # Output: [1, 3, 12, 0, 0]
    