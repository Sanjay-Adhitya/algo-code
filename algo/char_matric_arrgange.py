def gridChallenge(grid):
    indexgrid = []
    sorted_indexgrid = []
    for i in grid:
        temp = []
        for j in i:
            temp.append(ord(j))
        indexgrid.append(temp)
    
    for i in indexgrid:
        sorted_indexgrid.append(quick_sort(i))
    print(sorted_indexgrid)
    return check_if_sorted(sorted_indexgrid)
        
def quick_sort(s):
    if len(s) <= 1:
        return s
    p = s[len(s) // 2]  # Choose the pivot element from the middle
    l = [i for i in s if i < p]
    eq = [i for i in s if i == p]
    r = [i for i in s if i > p]

    return quick_sort(l)+eq+quick_sort(r)

def check_if_sorted(grid):
    row = 0
    col = 0
    while row < len(grid):
        while col < len(grid[row]):
            if row < len(grid) - 1 and grid[row][col] > grid[row+1][col]:
                return 'NO'
            col += 1
        col = 0  # Reset col to 0 for the next row
        row += 1
    return 'YES'

grid = ['vpvv', 'pvvv', 'vzzp', 'zzyy']

print(gridChallenge(grid))
