import sys
def check(target, n, k, a):
    L = n // 2
    diff = [0] * (n + 1)
    current_adds = 0
    total_ops = 0
    for i in range(n):
        current_adds += diff[i]
        current_val = a[i] + current_adds
        if current_val < target:
            needed = target - current_val
            total_ops += needed
            if total_ops > k:
                return False
            if i + L > n:
                return False
            current_adds += needed
            diff[i + L] -= needed
    return total_ops <= k
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    a = [int(x) for x in input_data[2:2+n]]
    low = a[0]
    high = a[-1] + k
    ans = low
    while low <= high:
        mid = (low + high) // 2
        if check(mid, n, k, a):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1 
    print(ans)
if __name__ == '__main__':
    solve()