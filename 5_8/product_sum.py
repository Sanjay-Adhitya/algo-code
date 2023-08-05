def product_sum(array):
    tot_mul = 1
    for i in range(0,len(array)):
        tot_mul *= array[i]
    for i in range(0,len(array)):
        array[i] = int(tot_mul/array[i])
    return array

print(product_sum([5,1,4,2]))