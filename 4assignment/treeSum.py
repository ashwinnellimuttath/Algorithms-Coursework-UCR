import heapq
n = int(input())
weights = [0] * n
adj = [[] for _ in range(n)]
maxWeight = [0] * n

for i in range(n):
    weights[i] = int(input())

for i in range(1, n):
    parent = int(input())
    adj[parent].append(i)

maxValue = [float("-inf")]

def dp_sum(node):
    childArray = []
    childArrayMax = []
    if maxWeight[node] != 0: 
        return maxWeight[node]

    max_child_sum = 0

    for child in adj[node]:
        a = dp_sum(child)
        # childSum += max(0,maxWeight[child])
        # heapq.heappush(childArrayMax,-maxWeight[child])
        heapq.heappush(childArray,-a)
        # childSum.append(maxWeight[child])
        # if node == 0:
        #     print(childSum,node,weights[child],child ,"here")
    childSum = 0
    c = 0
    # while len(childArray) and c < 2:
    #     c += 1
    #     childSum += max(0,-heapq.heappop(childArray))
    a,b = 0,0
    if len(childArray):
        a = max(0,-heapq.heappop(childArray) )
    if len(childArray):
        b = max(0,-heapq.heappop(childArray) )
    # aMax,bMax = 0,0
    # if len(childArrayMax):
    #     aMax = max(0,-heapq.heappop(childArrayMax) )
    # if len(childArrayMax):
    #     bMax = max(0,-heapq.heappop(childArrayMax) )
    
    # maxWeight[node] = max(maxWeight[node],  weights[node] + aMax + bMax)
    maxValue[0] = max(maxValue[0],  weights[node] + a + b)
    # maxWeight[node] = weights[node] + a + b
    return weights[node] + max(a,b)

# def dfs(node):
#     nodeWeight = weights[node]
#     for child in adj[node]:
#         dfs(child)
#         if maxWeight[child] > 0:
#             nodeWeight += maxWeight[child]
#     maxWeight[node] = max(nodeWeight,maxWeight[node])
    




    # nodeWeight = weights[node]
    # for child in adj[node]:
    #     dfs(child)
    #     if maxWeight[child] > 0:
    #         nodeWeight += maxWeight[child]
    # maxWeight[node] = nodeWeight



dp_sum(0)
print(maxValue[0])
# print((max(maxWeight)))
