arr = [1,2,3,4,5]

x = 0
y = len(arr) -1

while x < y:
    arr[x],arr[y] = arr[y], arr[x]
    x += 1
    y -= 1 

print(arr)