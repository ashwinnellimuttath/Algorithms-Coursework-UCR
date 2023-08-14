from math import log


a = float(input())
minValue = float("inf")

values = [ 1 +  x*.0001 for x in range(int((2 - 1)/.0001))]
for x in values:
    if log(x) == 0:
        continue
    f = ((x**2)/log(x)) + a * x
    minValue = min(f,minValue)

print( minValue)
