# def two_sum(array, sum):

#     # methd one hash table
#     diff = {}
#     for i in array:
#         if diff.get(sum-i):
#             return i, sum-i
#         else:
#             diff[i] = True
    
def two_sum(array, sum):
    array = sorted(array)
    r = 0
    l = len(array) -1

    while r<l:
        if array[r]+array[l] > sum:
            l-=1
        elif array[r]+array[l] < sum:
            r+=1
        else:
            return array[r],array[l]
    return None

print(two_sum([2,5,4,1],6))