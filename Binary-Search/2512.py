'''
문제 : 예산
출처 : https://www.acmicpc.net/problem/2512
카테고리 : #binary-search #max
'''


def binary_search(n, requests, budget):
    start, end = 0, max(requests)

    if sum(requests) <= budget:
        return max(requests)

    while start <= end:
        mid = (start + end) // 2

        temp = 0

        for i in range(n):
            temp += min(requests[i], mid)

        if temp <= budget:
            start = mid + 1
        else:
            end = mid - 1

    return end


def solution():
    n = int(input())

    requests = list(map(int, input().split()))
    budget = int(input())
    requests.sort()

    print(binary_search(n, requests, budget))


if __name__ == "__main__":
    solution()
