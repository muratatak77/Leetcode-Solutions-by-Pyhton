
def validTree(n, edges):
    
    if not edges:
        return False

    if len(edges) != n - 1:
        return False
    
    # Create an adjacency list.
    adj_list = [[] for _ in range(n)]

    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)
    
    print("adj_list : ", adj_list)

    # We still need a seen set to prevent our code from infinite
    # looping if there *is* cycles (and on the trivial cycles!)
    seen = set()
    print("seen :", seen)

    def dfs(node):
        if node in seen: 
            return

        seen.add(node)
        print("seen : ", seen)

        for nbr in adj_list[node]:
            dfs(nbr)

    dfs(edges[0][0])
    
    print("seen len : ", len(seen) , " -  n :", n)

    return len(seen) == n

n = 5
edges = [[0,1], [0,2], [0,3], [1,4]]
edges = [[0,1], [1,2], [2,3], [1,3]]

res = validTree(n,edges)
print("res : " , res)