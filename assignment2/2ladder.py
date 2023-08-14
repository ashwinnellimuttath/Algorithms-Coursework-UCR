import heapq

def find_kth_intersection(ladders, k):
    n = len(ladders)
    events = []
    for i in range(n):
        x1, y1, x2, y2 = ladders[i]
        if x1 > x2:
            x1, y1, x2, y2 = x2, y2, x1, y1
        events.append((x1, i, 1, y1, y2))
        events.append((x2, i, -1, y1, y2))
    events.sort()
    active = []
    for x, i, t, y1, y2 in events:
        if t == 1:
            heapq.heappush(active, (-y1, i))
        else:
            # active.remove((-y1, i))
            heapq.heapify(active)
        for _, j in active:
            if i < j:
                k -= 1
                if k == 0:
                    return i+1, j+1
    return None

# -1 -1 1 1
# 1 0 2 0
# 0 1 1 0
ladders = [(-1, -1, 1, 1), (1, 0, 2, 0), (0, 1, 1, 0)]
k = 2
indices = find_kth_intersection(ladders, k)
print(indices) 