def mat_spriral(mat):

    sr, er = 0, len(mat) - 1
    sc, ec = 0, len(mat[0]) - 1

    while sr <= er and sc <= ec:
        
        # right ->
        
        # down  \/
        # left  /\
        # top   <-


mat_spriral(
    [
        [ 1, 2, 3, 4, 5],
        [ 6, 7, 8, 9,10],
        [11,12,13,14,15]
    ]
)