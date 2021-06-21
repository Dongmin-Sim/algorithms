from collections import deque
import time

first = time.time()

n, l = map(int, input().split())
order = list(map(int, input().split()))

# n, l = 12, 3
# order = [1, 5, 2, 3, 6, 2, 3, 7, 3, 5, 2, 6]

queue = deque()

for idx in range(n):
    while queue and queue[-1][1] > order[idx]:
        queue.pop()
    while queue and idx - queue[0][0] >= l:
        queue.popleft()

    queue.append((idx, order[idx]))
    print(queue[0][1], end=' ')


print('time : ', time.time() - first)