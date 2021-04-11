def sudokuCheck(grid):
    #edge cases
    if not grid:
        return False
    
    #rows by rows checking 
    hset = set()
    for i in range(9):
        for j in range(9):
            if grid[i][j] in hset:
                return False
            else:
                hset.add(grid[i][j])
        hset = set()
            
    #cols by cols checking
    hset = set()
    for i in range(9):
        for j in range(9):
            if grid[j][i] in hset:
                return False
            else:
                hset.add(grid[j][i])
        hset = set()
    
    
    #3 by 3 check
    '''
        0,0 0,1 0,2 | 0,3    0,5 | 0,6   0,8
        1,0 1,1 1,2 | 1,3    1,5
        2,0 2,1 2,2 | 2,3    2,5 |       2,8
        
        3,0
    '''
    subs = [range(0,3), range(3,6), range(6,9)]

    subgrids = [] 
    for x in subs:
        for y in subs:
            subgrids.append([x,y])


    # subgrids = [(x,y) for x in subs for y in subs]
    # print("subgrids : ", subgrids)

    for (row_range, column_range) in subgrids:

        print("row_range : ", row_range)
        print("column_range : ", column_range)

        hset = set()
        for i in row_range:
            for j in column_range:              
                if grid[i][j] in hset:
                    return False
                else:
                    hset.add(grid[i][j])
    
    return True
    

grid = [
     
     0  1  2   3  4  5   6  7  8

 0   [8, 3, 5,  4, 1, 6,  9, 2, 7],

 1   [2, 9, 6,  8, 5, 7,  4, 3, 1],

 2   [4, 1, 7,  2, 9, 3,  6, 5, 8],



 3   [5, 6, 9,  1, 3, 4,  7, 8, 2],

 4   [1, 2, 3,  6, 7, 8,  5, 4, 9],

 5   [7, 4, 8,  5, 2, 9,  1, 6, 3],



 6   [6, 5, 2,  7, 8, 1,  3, 9, 4],

 7   [9, 8, 1,  3, 4, 5,  2, 7, 6],

 8   [3, 7, 4,  9, 6, 2,  8, 1, 5]

]

res = sudokuCheck(grid)
print("res : ", res)
