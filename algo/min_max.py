def miniMaxSum(arr):
    
    """
    Given five positive integers, find the minimum and maximum values 
    that can be calculated by summing exactly four of the five integers. 
    Then print the respective minimum and maximum values as a single 
    line of two space-separated long integers.
    """

    min = arr[0]
    max = arr[0]
    total = 0
    for i in arr:
        if i < min:
            min = i
        if i > max:
            max = i
        total += i
    print(str(total - max) +" "+str(total - min))

miniMaxSum([1,3,5,7,9])