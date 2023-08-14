n, k = map(int, input().split())
ladders = []
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    ladders.append(((x1, y1), (x2, y2)))

intersections = []
for i in range(n):
    for j in range(i+1, n):
        p1, p2 = ladders[i]
        q1, q2 = ladders[j]
        m1 = (p2[1] - p1[1]) / (p2[0] - p1[0]) if p2[0] != p1[0] else float('inf')
        m2 = (q2[1] - q1[1]) / (q2[0] - q1[0]) if q2[0] != q1[0] else float('inf')
        if m1 == m2:
            continue
        b1 = p1[1] - m1 * p1[0]
        b2 = q1[1] - m2 * q1[0]
        x = (b2 - b1) / (m1 - m2)
        # if x < min(p1[0], p2[0]) or x > max(p1[0], p2[0]) or x < min(q1[0], q2[0]) or x > max(q1[0], q2[0]):
        #     continue
        y = m1 * x + b1
        intersections.append((x, y, i, j))

intersections.sort()
# print(intersections)
i, j = intersections[k-1][2], intersections[k-1][3]
print(i+1, j+1)
