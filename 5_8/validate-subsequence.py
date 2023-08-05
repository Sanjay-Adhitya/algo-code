def validate_sum_seq(array, subarray):
    p = 0
    for i in array:
        if p == len(subarray):break

        if subarray[p] == i:
            p+=1
    return p == len(subarray)

print(validate_sum_seq([1,2,3,4,5,6,7,8,9,0],[1,5,1]))