# Input (you choose the data structure that you take in):
#   Server 1              Server 2
# Time   Users          Time   Users
#   0      5              3      10
#   3      10             10     3
#   15     2        >     20     8
#   25     15             30     5

#   Server 1              Server 2
# Time   Users          Time   Users
#  > 0      5             35      10
#   3      10             
#   15     2             
#   25     15            

# Output (whatever data structure you ended up choosing):
# Time   Users
#   0      5
#   3      20
#   10     13
#   15     5
#   20     10
#   25     23
#   30     20


def match_output(server1, server2):

    result = []
    
    i = 0
    j = 0
    while i < len(server1) and j < len(server2):
        
        print(" i : ", i , " - j : ", j)
        
        if server1[i][0] < server2[j][0]:
            if server1[i][0] == 0 and server1[i] == 0:
                result.append([server1[i][0], server1[i][1]])

            elif server1[i][0] < server2[j-1][0]:
                result.append([server1[i][0], server1[i][1]+server2[j][1]])
                
            i += 1
        elif server1[i][0] == server2[j][0]:
            result.append([server1[i][0], server1[i][1]+server2[j][1]])
            i += 1
            j += 1
        else:
            
            result.append([server1[i][0], server1[i][1]])
            j += 1
    
    print("result : " , result)
            


server1 = [[0,5],[3,10],[15,2],[25,15]] 
server2 = [[3,10],[10,3],[20,8],[30,5]]


match_output(server1, server2)