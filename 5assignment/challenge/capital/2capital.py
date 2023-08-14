from collections import defaultdict
 
def dfs(u, adj, visited):
    stack = [u]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            for neighbor in adj[v]:
                if not visited[neighbor]:
                    stack.append(neighbor)
 
def findAllMotherVertices(adj,trans_adj):
    n = len(adj)
    visited = [False for _ in range(n)]
    last_dfs = -1
    
    # motherVertex = []



    for u in range(n):
        if not visited[u]:
            dfs(u, adj, visited)
            last_dfs = u


    # dfs(last_dfs, adj, visited)
    # for u in range(n):
    #     if not visited[u]:
    #         return []





    visited = [False for _ in range(n)]
    dfs(last_dfs, adj, visited)
    for u in range(n):
        if not visited[u]:
            return []
    motherVertex = last_dfs
    visited = [False for _ in range(n)]
    dfs(motherVertex, trans_adj, visited)
    ans = []
 



    for u in range(n):
        if visited[u]:
            ans.append(u)
    return ans


n, m = map(int, input().split())
adjacency_list = [ [] for  i in range(n)]
trans_adj = [[] for _ in range(n)]
# adjacency_list = defaultdict(list)
# trans_adj = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    trans_adj[a-1].append(b-1)
    adjacency_list[b-1].append(a-1)
# print(adjacency_list)
motherVertices = findAllMotherVertices(adjacency_list,trans_adj)
for i in range(len(motherVertices)):
    motherVertices[i] += 1

print(len(motherVertices))
print(" ".join(map(str, motherVertices)))