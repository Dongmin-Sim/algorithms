'''
문제 : 벽 부수고 이동하기 
https://www.acmicpc.net/problem/2206
'''
import sys
from collections import deque


def bfs(n, m, graph, d, visited):
    q = deque([(0, 0, 1)])

    while q:
        cur = q.popleft()
        x, y, count = cur

        visited[x][y] = count

        for dx, dy in d:
            nx = dx + x
            ny = dy + y

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] != -1:
                continue
            if graph[nx][ny] == '1':
                continue

            q.append((nx, ny, count + 1))

    return visited[n-1][m-1]


def solution(n, m, graph):
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited = [[-1 for _ in range(m)] for _ in range(n)]

    min_dist = bfs(n, m, graph, d, visited[::])

    # 전체 브루트 포스 1인 벽을 모두 부시고 비교
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '1':
                graph[i][j] = '0'

                temp = bfs(n, m, graph, d, visited[::])

                if temp > 0:
                    if min_dist != -1:
                        min_dist = min(min_dist, temp)
                    elif min_dist == -1:
                        min_dist = temp

                graph[i][j] = '1'

    return min_dist


def main():
    n, m = map(int, input().split())

    graph = []
    for _ in range(n):
        graph.append(list(sys.stdin.readline().strip()))

    print(solution(n, m, graph))


if __name__ == '__main__':
    main()
