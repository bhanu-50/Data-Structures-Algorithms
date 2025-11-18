#Kadane’s Algorithm — Find the maximum subarray sum

#solution 1:
def subarray_sum(arr):
    max_sum = arr[0]
    sum_val = 0
    for i in arr:
        sum_val += i
        max_sum = max_sum if max_sum>sum_val else sum_val
        if sum_val < 0:
            sum_val = 0
    return max_sum

#solution 2:
def subarray_sum2(arr):
    max_sum1 = arr[0]
    sum_val1 = arr[0]
    for i in arr[1:]:
        sum_val1 = max(i,i+sum_val1)
        max_sum1 = max(sum_val1,max_sum1)
    return max_sum1

arr = [-2,1,-3,4,-1,2,1,-5,4]
result = subarray_sum2(arr)
print(f"The maximum subarray sum is: {result}")
        