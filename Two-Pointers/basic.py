# 데이터의 개수, 찾고자 하는 부분합
n, m = 5, 5

data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        #
        interval_sum += data[end]
        end += 1

    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)


# 두 리스트 정렬 문제
n, m = 3, 4

a = [1, 3, 5]
b = [2, 4, 6, 8]

result = [] * (n+m)
