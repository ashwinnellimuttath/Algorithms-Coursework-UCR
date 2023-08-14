C = 8

profit = [4,4,7,1]
weight = [5,2,3,1]

dp = [[0] * (C + 1) for _ in profit]
# print(dp)

def dfsHelper(i,capacity):
    # print(i)
    if i >= len(profit):
        return 0

    maxProfit = dfsHelper(i + 1, capacity)
    newCapacity = capacity - weight[i]

    if newCapacity >=0:
        p = profit[i] + dfsHelper(i + 1, newCapacity)
        maxProfit = max(maxProfit,p)

    return maxProfit

    



print(dfsHelper(0,C))



    