def plusMinus(arr):

    """
    Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
    Print the decimal value of each fraction on a new line with places after the decimal.
    """
    a,b,c = 0,0,0
    for i in range(len(arr)):
        if arr[i] == 0:
            a += 1
            continue
        if arr[i] > 0:
            b += 1
        else:
            c += 1
    print(a,b,c)
    print(format(a/len(arr), f".{6}f"))
    print(format(b/len(arr), f".{6}f"))
    print(format(c/len(arr), f".{6}f"))

arr = [-4, 3, -9, 0, 4, 1]

plusMinus(arr)