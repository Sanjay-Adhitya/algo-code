def bribeQueue(arr):
    for i in range(len(arr)):
        if i+1 < len(arr)-1 and arr[i] > arr[i+1]:
            arr = swap(arr, i)       
    return arr

def swap(arr, i):
    t = arr[i]
    arr[i]= arr[i+1]
    arr[i+1] = t
    return arr

arr =  [2, 1, 5, 3, 4]
print(bribeQueue(arr=arr))
