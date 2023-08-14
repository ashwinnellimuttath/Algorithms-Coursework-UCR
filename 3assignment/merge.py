import heapq

n = int(input())
minHeap = []
for i in range(n):
     minHeap.append(int(input()))

# minHeap = [3,8,1,6]

heapq.heapify(minHeap)
# print(minHeap)
total = 0
while minHeap:
    l1 = heapq.heappop(minHeap)
    if minHeap:
        l2 = heapq.heappop(minHeap)
        total += l1 + l2

        addSum = l1 + l2
        total += addSum
        
        heapq.heappush(minHeap,addSum)
    # else:
    #     total += l1

print(total)
