from collections import deque
import time
first = time.time()
# 접시수, 초밥가짓수, 연속 접시 수, 쿠폰 번호
# n, d, k, c = map(int, input().split())
# table = list(map(int, input().split()) for _ in range(n))

n, d, k, c = 8, 30, 4, 30
table = [7, 9, 7, 30, 2, 7, 9, 25]

temp = deque()
answer = 0

for idx in range(n-1, -k-1, -1):
    if c in temp:
        answer = max(answer, len(set(temp)))
    else:
        answer = max(answer, len(set(temp)) + 1)

    # 윈도우 길이 k이상 일 경우 맨 앞 요소 pop
    while temp and len(temp) >= k:
        temp.popleft()

    temp.append(table[idx])

print(answer)


print('time : ', time.time() - first)