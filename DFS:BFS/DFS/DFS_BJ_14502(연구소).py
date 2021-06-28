import sys

input = sys.stdin.readline
n, m = map(int, input().split())
labs = [list(map(int, input().split())) for _ in range(n)]

# 테스트 케이스
# n, m = 7, 7
# labs = [[2, 0, 0, 0, 1, 1, 0],
#         [0, 0, 1, 0, 1, 2, 0],
#         [0, 1, 1, 0, 1, 0, 0],
#         [0, 1, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 1, 1],
#         [0, 1, 0, 0, 0, 0, 0],
#         [0, 1, 0, 0, 0, 0, 0]]

temp = [[0] * m for _ in range(n)]

d = (-1, 0), (1, 0), (0, -1), (0, 1)

score = 0


# 바이러스 dfs
def virus_dfs(x, y):
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus_dfs(nx, ny)


# 안전영역 계산
def safty_zone():
    zone = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                zone += 1
    return zone


# 벽 세우기 & 답 구하기
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
