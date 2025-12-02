#Rotate an array k times (both left and right rotation
#solution 1:
def reverse(arr,start,end):
   
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
        
        
def rotate(arr,k):
    n = len(arr)
    k = k % n
    
    reverse(arr,0,n-1)
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    return arr
    
#solution 2:
def rotate_arr(arr,k):
    while k>0:
        temp = arr[0]
        for i in range(len(arr)-1):
            arr[i] = arr[i+1]
            
        arr[len(arr)-1] = temp
        k -=1
    return arr
    

arr = [1,2,3,4,5,6,7,8,9]
print(rotate(arr,3))

    