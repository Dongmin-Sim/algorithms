from collections import deque

n, k = map(int, input().split())

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            break
        for cal in (x + 1, x - 1, x * 2):
            if 0 <= cal <= 100000 and sec[cal] == 0:
                sec[cal] = sec[x] + 1
                q.append(cal)

    return sec[k]


sec = [0] * 100001
print(bfs())
