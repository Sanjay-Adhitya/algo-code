def diagonalDifference(arr):
    # sum_right_diag = sum(arr[i][i] for i in range(len(arr)))
    # sum_left_diag = sum(arr[i][len(arr[i])-(i+1)] for i in range(len(arr)))
    
    sum_right_diag, sum_left_diag = 0, 0

    for i in range(len(arr)):
        sum_right_diag += arr[i][i]
    for i in range(len(arr)):
        sum_left_diag += arr[i][len(arr[i])-(i+1)] 

    if  sum_right_diag > sum_left_diag:
        return sum_right_diag - sum_left_diag
    else:
        return sum_left_diag - sum_right_diag 
print(diagonalDifference(
    [
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ]
))