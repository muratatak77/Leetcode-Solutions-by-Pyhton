# import requests
# import mysql.connector
# import pandas as pd

'''
file = 

AFKPU
BGLQV
CHMRW
DINSX
EJOTY

2 dimen array

end of line = EJOTY

convert arr
E = (0,0)
J = (0,1)

DINSX

D = 1,0
I = 2,0

'''

def find_char():
    
    f = open("file.txt", "r")
    lines = f.readlines()

    target_x = int(lines[0][1].strip())
    target_y = int(lines[0][3].strip())
    
    arr = []
    for i in range(1,len(lines)):
        item = lines[i].replace("\n", "")
        item = list(item)
        arr.append(item)
        
    arr = arr[::-1]
    return arr[target_y][target_x]

    # row_size = len(arr)
    # col_size = len(arr[0])
    
    # for i in range(row_size):
    #     for j in range(col_size):
    #         if i == target_y and j == target_x:
    #             return arr[i][j]
    
    
res = find_char()
print("res : ", res)