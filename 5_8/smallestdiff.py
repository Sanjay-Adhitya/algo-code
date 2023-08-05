def smallest_diff(arr1,arr2):

    i1 = 0
    i2 = 0
    diff = {}
    while i1 < len(arr1) and i2 < len(arr2):
        diff[arr1[i1] - arr2[i2]] = [arr1[i1] , arr2[i2]]
        if arr1[i1] < arr2[i2]:
            i1 += 1
        elif arr1[i1] > arr2[i2]:
            i2 += 1
        else:
            return [arr1[i1] , arr2[i2]]
    arr_diff = list(diff.keys())
    min = -1 * arr_diff[0] if arr_diff[0] < 0 else arr_diff[0] 
    for i in range(1,len(arr_diff)):
        i_ = -1 * arr_diff[i] if arr_diff[i] < 0 else arr_diff[i] 
        if min > i_:
            min = i_
    return min
    
print(smallest_diff([-1,3,5,10,20,28],[15,17,27,134,135]))