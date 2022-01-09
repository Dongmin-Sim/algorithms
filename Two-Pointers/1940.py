


n = int(input())
m = int(input())

shield = list(map(int, input().split()))
i, j = 0, n-1
ans = 0

shield.sort()

while i < j:
    sum_num = shield[i] + shield[j]
    if sum_num == m:
        ans += 1
        i += 1
        j -= 1
    elif sum_num < m:
        i += 1
    else:
        j -= 1

print(ans)