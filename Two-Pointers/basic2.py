n, m = 3, 4

a = [1, 3, 5]
b = [2, 4, 6, 8]

result = [0] * (n+m)
i = 0
j = 0
k = 0

while i < (len(a)) or j < (len(b)):
    # a의 원소가 들어가는 경우
    if (i <len(a) and a[i] <= b[j]) or j >= (len(b)):
        result[k] = a[i]
        i += 1
    else:
        result[k] = b[j]
        j += 1
    k += 1

print(result)