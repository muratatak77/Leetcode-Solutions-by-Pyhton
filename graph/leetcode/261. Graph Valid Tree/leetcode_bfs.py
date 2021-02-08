'''
    we can start to build a adjancency list  to reach all neighbours of a node.
    after we need a set to check visiting previous current node.
    
'''
from collections import deque

def validTree(n, edges):

    if not edges:
        return False

    if len(edges) != n-1:
        return False

    # we need adj list to iterator and check all neighbors in graph
    adj_list = [[] for _ in range(n)]
    for src,dst in edges:
        adj_list[src].append(dst)
        adj_list[dst].append(src)

    print("adj_list ;", adj_list)

    #we need a set to check previous visited node. 
    #If we have visited node , we can return and we will exit the dfs call stack
    seen = {adj_list[0][0]}
    q = deque([adj_list[0][0]])

    print("seen : ", seen)
    print("q : ", q)

    while q:
        node = q.popleft()
        for neighbour in adj_list[node]:
            if neighbour in seen:
                continue
            seen.add(neighbour)
            q.append(neighbour)

    return len(seen) == n


n = 5
edges = [[0,1], [0,2], [0,3], [1,4]]
# edges = [[0,1], [1,2], [2,3], [1,3]]
# edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]

res = validTree(n,edges)
print("res : " , res)


'''
    T(N) :  O(N) > push/pop vertices
            O(M) > looking at adjlist of each vertex.
                Total O(Degree(u)) Degree of that node. > 2m = O(m)     
                result = O(M+N)
            
    S(N) : O(N)

'''