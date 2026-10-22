x = int(input())
y = int(input())
a = int(input())
b = int(input())
m = int(input())
d = int(input())
dist_both = abs(x) + abs(x - y) + abs(y)
can_combine = (a + b <= m) and (dist_both <= d)

can_x_alone = (a <= m) and (2 * abs(x) <= d)
can_y_alone = (b <= m) and (2 * abs(y) <= d)

if can_combine:
    print(1)
elif can_x_alone and can_y_alone:
    print(2)
else:
    print(-1)
