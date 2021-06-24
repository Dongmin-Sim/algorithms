n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
count = 0

for i in range(len(a)):
    if a[i] < b[i] and count < k:
        a[i], b[i] = b[i], a[i]
    else:
        continue
    count += 1

print(sum(a))