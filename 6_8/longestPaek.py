# def long_peak(array):
#     peek = 0
#     for i in range(0, len(array) - 1):
#         if array[i] > array[i+1]: 
#             if peek < array[i]:peek = array[i]
#     return peek
       
# print(long_peak([1,2,3,3,4,0,10,6,5,-1,-3,12,3]))

# def long_peak(array):
#     peek = []
#     for i in range(0, len(array) - 2):
#         if array[i] < array[i+1] > array[i+2]: 
#             peek.append([array[i+1],i+1])
#     if len(peek) > 1:
#         index = 0
#         for i in range(1,len(peek)):
#             if peek[index][0] < peek[i][0]:
#                 index = i
#         return peek[index][1]

def long_peak(array):
    l_peek = 0
    i = 1
    while i < len(array) -1:
        ispeek = array[i-1] < array[i] > array[i+1]
        if not ispeek:
            i+=1
            continue
        # here is the currunt solution different 
        # the logest does not mean the 
        # highest number but the number that has the 
        # many adjest number which are smaller then this number 
        # left
        lefti = i-2
        while lefti >= 0 and array[lefti] < array[lefti + 1]:
            lefti -= 1
        
        righti = i+2
        while righti >= len(array) and array[righti] < array[righti - 1]:
            righti += 1
        
        # current peek len
        curpeek = righti - lefti -1
        l_peek = l_peek if l_peek>curpeek else curpeek
        i = righti
    return l_peek

print(long_peak([1,2,3,3,4,0,10,6,5,-1,-3,2,3]))



