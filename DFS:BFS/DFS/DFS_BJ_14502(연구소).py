import sys
from itertools import combinations

input = sys.stdin.readline

# n, m = map(int, input().split())
n, m = 7, 7



# labs = [list(map(int, input().split())) for _ in range(n)]
labs = [[2, 0, 0, 0, 1, 1, 0],
        [0, 0, 1, 0, 1, 2, 0],
        [0, 1, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0]]

temp = [[0] * m for _ in range(n)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
d = (-1, 0), (1, 0), (0, -1), (0, 1)


score = 0


# 바이러스 dfs
def virus_dfs(x, y):
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus_dfs(nx, ny)


# 안전영역 개
def safty_zone():
    zone = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                zone += 1
    return zone


# 벽세우기
def solution(count):
    global score

    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = labs[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus_dfs(i, j)
        score = max(score, safty_zone())
        return
    # 모든 구간(0)에 대해 벽 세우기
    for i in range(n):
        for j in range(m):
            if labs[i][j] == 0:
                labs[i][j] = 1
                count += 1
                solution(count)
                labs[i][j] = 0
                count -= 1

solution(0)
print(score)
