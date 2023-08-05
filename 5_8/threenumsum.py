def threenumsum(array, sum):
    
    diff = []
    l=1
    r=len(array) - 1
    for i in array:
        while l<r:
            if i+array[r]+array[l] > sum:
                r-=1
            elif i+array[r]+array[l] < sum:
                l+=1
            else:
                diff.append([i,array[r],array[l]])
                r-=1
                l+=1
    print(diff)
threenumsum([1,2,3,4,5],8)