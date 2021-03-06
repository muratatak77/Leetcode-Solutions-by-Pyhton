
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
    seen = set()

    def dfs(node):
        if node in seen:
            return
        seen.add(node)
        print("node : ", node)
        for nbr in adj_list[node]:
            dfs(nbr)

    dfs(edges[0][0])
    return len(seen) == n


n = 5
edges = [[0,1], [0,2], [0,3], [1,4]]
edges = [[0,1], [1,2], [2,3], [1,3]]
# edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]

res = validTree(n,edges)
print("res : " , res)