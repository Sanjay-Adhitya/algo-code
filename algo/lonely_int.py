def lonelyinteger(a):
    
    """
    Given an array of integers, where all elements 
    but one occur twice, find the unique element.
    """
    twice_dict = dict()
    single = None
    for i in a:
        if twice_dict.get(i):
            print("in")
            twice_dict[i] += 1
            if single == i:
                single = None
        else:
            print("out")
            twice_dict[i] = 1
            single = i

    for i in twice_dict:
        if twice_dict[i] < 2:
            return i

print(lonelyinteger(
    [1,2,2,4,5,5,1]
)
)