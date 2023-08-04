
def find_unique(array):
    count = {}
    for i in array:
        if count.get(i):
            count[i] += 1
        else:
            count[i] = 1
    for i in count.keys():
        if count[i] == 1:
            return i

print(find_unique([1,2,3,1,2,4,3]))