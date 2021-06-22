from collections import deque
import time
first = time.time()
# 접시수, 초밥가짓수, 연속 접시 수, 쿠폰 번호
# n, d, k, c = map(int, input().split())
# table = list(map(int, input().split()) for _ in range(n))

n, d, k, c = 8, 30, 4, 30
table = [7, 9, 7, 30, 2, 7, 9, 25]

pos_var = []
temp = deque()
set_count = 0

for idx in range(n-1, -k-1, -1):
    if len(temp) > k:
        temp.popleft()

    # k 보다 작은 가지수가 있음
    if len(temp) == k and set_count <= len(set(temp)):
        set_count = len(set(temp))
        pos_var.append(set(temp))

    temp.append(table[idx])


answer = 0

for pos in pos_var:
    if c in pos and answer < len(pos):
        answer = len(pos)
    else:
        answer = len(pos) + 1

print(len(pos_var), pos_var)
print(answer)


print('time : ', time.time() - first)