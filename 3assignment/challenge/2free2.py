import heapq

n, m = map(int, input().split())
yihan_days = list(int(input()) for _ in range(n))
students = [tuple(map(int, input().split())) for _ in range(m)]
students.sort()

max_students = 0
assigned_students = []
i = 0
for day in sorted(yihan_days):
    while assigned_students and assigned_students[0] < day:
        heapq.heappop(assigned_students)
    while i < len(students) and students[i][0] <= day  :
        heapq.heappush(assigned_students,(students[i][1]))
        i += 1

    while len(assigned_students):
        end = heapq.heappop(assigned_students)
        if end >= day:
            max_students += 1
            break

print(max_students)


# if previosMaxbenifit > currentMaxbenifit:
#     benifit, count, items = previosMaxbenifit, prevCount, previosItems
# elif previosMaxbenifit < currentMaxbenifit:
#     benifit, count, items = currentMaxbenifit, currentCount + 1, currentItems.append(i)
# else:
#      benifit, count, items = currentMaxbenifit, prevCount, items