'''
문제 : 바이러스
https://www.acmicpc.net/problem/2606
'''
import sys
from collections import deque


def solution(n: int, k: int, nodes: list) -> int:
    visited = [0 for _ in range(n+1)]
    computer = [[] for _ in range(n+1)]

    for parent, child in nodes:
        computer[parent].append(child)
        computer[child].append(parent)

    que = deque()
    que.append(1)

    while que:
        cur = que.popleft()
        visited[cur] = 1

        for adjNode in computer[cur]:
            if visited[adjNode] != 0:
                continue

            visited[adjNode] = 1
            que.append(adjNode)

    return sum(visited) - 1


def main():
    input = sys.stdin.readline

    n = int(input())
    k = int(input())

    nodes = []

    for _ in range(k):
        a, b = map(int, input().split())
        nodes.append((a, b))

    print(solution(n, k, nodes))


if __name__ == '__main__':
    main()
