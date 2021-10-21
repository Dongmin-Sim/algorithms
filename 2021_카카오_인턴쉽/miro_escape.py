import heapq


def solution(n, start, end, roads, traps):
    graph = [[] for _ in range(n+1)]
    # 방문 여부?
    visited = [False] * (n+1)
    INF = int(1e9)

    distance = [INF] * (n+1)

    for road in roads:
        node1, node2, cost = road[0], road[1], road[2]
        # 정방향
        graph[node1].append((node2, cost, 1))
        # 역방향
        graph[node2].append((node1, cost, 0))

    graph_status = True

    q = []
    heapq.heappush(q, (0, start))

    visited[start] = True

    while q:
        dist, now = heapq.heappop(q)

        # 방문한 노드가 trap 노드라면
        if now in traps:
            # graph_status는 바뀜
            graph_status = not graph_status
            visited[now] = False

        for i in graph[now]:
            if i[2] == graph_status:
                visited[i[0]] = True
                cost = dist + i[1]
                # 여기서 오류
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
            else:
                continue

    return distance[end]


# def solution(n, start, end, roads, traps):
#     INF = int(1e9)
#     graph = [[] for _ in range(n + 1)]
#     visited = [False] * (n + 1)
#     dist = [INF] * (n+1)

#     for road in roads:
#         node1, node2, cost = road[0], road[1], road[2]
#         graph[node1].append((node2, cost, 1))
#         graph[node2].append((node1, cost, 0))

#     def smallest_node():
#         min_value = INF
#         index = 0
#         for i in range(1, n + 1):
#             if dist[i] < min_value and not visited[i]:
#                 min_value = dist[i]
#                 index = i

#         return index

#     dist[start] = 0
#     visited[start] = True


#     return

print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
