def square_sort(array):
    l = 0
    r = len(array) -1
    sorted_array = sorted(array)
    square_sorted_array = [0]*len(array)
    index = len(array) -1
    while l<r:
        if abs(sorted_array[l]) > abs(sorted_array[r]):
            square_sorted_array[index] = sorted_array[l]*sorted_array[l]
            l+=1
        else:
            square_sorted_array[index] = sorted_array[r]*sorted_array[r]
            r-=1
        index -= 1
        
    return square_sorted_array

print(square_sort([-1,-2,-4,1,2,3,4]))