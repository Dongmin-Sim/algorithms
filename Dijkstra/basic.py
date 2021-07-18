import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
dist = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if dist[i] < min_value and not visited[i]:
            min_value = dist[i]
            index = i

    return index


def dijkstra(start):
    dist[start] = 0
    visited[start] = True

    # start 노드에 연결되어있는 간선 정보 불러오기
    for j in graph[start]:
        dist[j[0]] = j[1]
    for _ in range(n-1):
        now_node = smallest_node()
        visited[now_node] = True
        for j in graph[now_node]:
            cost = dist[now_node] + j[1]
            if cost < dist[j[0]]:
                dist[j[0]] = cost


dijkstra(start)

for i in range(1, n + 1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
