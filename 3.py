import math
s = int(input())
p = int(input())
M = p // 2
max_a = min(M // 2, int(math.isqrt(s)))
count = 0
for a in range(1, max_a + 1):
    max_b = min(M - a, s // a)
    if max_b >= a:
        count += (max_b - a + 1)
print(count)