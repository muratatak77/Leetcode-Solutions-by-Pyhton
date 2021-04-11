
good_puzzle = [
    [8, 3, 5, 4, 1, 6, 9, 2, 7],
    [2, 9, 6, 8, 5, 7, 4, 3, 1],
    [4, 1, 7, 2, 9, 3, 6, 5, 8],
    [5, 6, 9, 1, 3, 4, 7, 8, 2],
    [1, 2, 3, 6, 7, 8, 5, 4, 9],
    [7, 4, 8, 5, 2, 9, 1, 6, 3],
    [6, 5, 2, 7, 8, 1, 3, 9, 4],
    [9, 8, 1, 3, 4, 5, 2, 7, 6],
    [3, 7, 4, 9, 6, 2, 8, 1, 5]
]

def isValidate(good_puzzle):
    #edge cases
    if not good_puzzle:
        return False
    
    row_size = len(good_puzzle[0])
    col_size = len(good_puzzle)
    
    
    # hash_set = set()
    # for i in range(row_size):
    #     for j in range(col_size):
    #         if good_puzzle[i][j] in hash_set:
    #             return False
    #         else:
    #             hash_set.add(good_puzzle[i][j])
            
    #         if j == col_size - 1:
    #             hash_set = set()
            

    # hash_set = set()
    # for i in range(row_size):
    #     for j in range(col_size):
    #         if good_puzzle[j][i] in hash_set:
    #             return False
    #         else:
    #             hash_set.add(good_puzzle[j][i])
            
    #         if j == col_size - 1:
    #             hash_set = set()
    
    
    hash_set = set()
    mult = 0
    for i in range(0,9,3):
        for j in range(0,9,3):


            print(" i : ", i , " - j : ", j)
            k = 0
            while k = 3:
                 

            if good_puzzle[i][j] in hash_set:
                return False
            else:
                hash_set.add(good_puzzle[i][j])


    print("hash_set: ", hash_set)
    if len(hash_set) < 9:
        return False
        
    return True

    

good_puzzle = [

    [8, 3, 5,  4, 1, 6, 9, 2, 7],
    [2, 9, 6,  8, 5, 7, 4, 3, 1],
    [4, 1, 7,  2, 9, 3, 6, 5, 8],

    [5, 6, 9, 1, 3, 4, 7, 8, 2],
    [1, 2, 3, 6, 7, 8, 5, 4, 9],
    [7, 4, 8, 5, 2, 9, 1, 6, 3],
    [6, 5, 2, 7, 8, 1, 3, 9, 4],
    [9, 8, 1, 3, 4, 5, 2, 7, 6],
    [3, 7, 4, 9, 6, 2, 8, 1, 5]
]
res = isValidate(good_puzzle)
print("res: ", res)    
    