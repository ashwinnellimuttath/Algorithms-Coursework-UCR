n, k = map(int, input().split())
 
classes = []
for i in range(n):
    s, t = map(int, input().split())
    classes.append((s, t))
 
# print(classes)
 
# classes = [(4, 6), (1, 10), (6, 9), (7, 8), (2, 4), (1, 10)]
# k = 1
 
 
 
 
 
def schedule_intervals(intervals, k):
    intervals.sort(key=lambda x: (x[1],x[0]))
 
    resources = [(-float('inf'), -float('inf'))] * k
    # resources = [(0,0)] * k
    
    count = 0
    
    for interval in intervals:
        start, end = interval
        
        # if res[1] == -float("inf") else start < res[1] + 1 
        # print(start,"start",resources)
        if all(start <= res[1] for res in resources):
            continue
        
        # for i in range(k):
        #     if end <= resources[i][1] :
        #         resources[i] = interval
        #         break
        # else:
        latest = max((r for r in resources if r[1] < start), key=lambda x: x[1])
        # print(latest,"latest",resources.index(latest))
        resources[resources.index(latest)] = interval
 
        
        # print(resources)
        count += 1
        # print((start,end),"start - end")
    # print(resources)
    return count
 
print(schedule_intervals(classes,k + 1))