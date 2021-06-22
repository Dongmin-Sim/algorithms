import sys
input = sys.stdin.readline

n, s = map(int, input().split())
order = list(map(int, input().split()))

# 방법 1
def solution(n, s, order):
    interval_sum, answer, end = 0, 0, 0

    for start in range(n):
        while interval_sum < s and end <= n:
            if end == n:
                end += 1
                break
            interval_sum += order[end]
            end += 1

        length = end - start

        if interval_sum >= s:
            if answer == 0 or answer > length:
                answer = length
        interval_sum -= order[start]

    return answer


# 방법 2 : interval_sum을 배열의 첫번째 값으로, answer를 inf으로
def solution2(n, s, order):
    interval_sum = order[0]
    answer = float('inf') # sys.maxsize도 가능
    end = 0

    for start in range(n):
        while interval_sum < s and end < n:
            end += 1
            if end == n:
                break
            interval_sum += order[end]

        length = end - start + 1

        if interval_sum >= s:
            answer = min(answer, length)

        interval_sum -= order[start]

    if answer == float('inf'):
        return '0'
    else:
        return answer


# 테스트 케이스
print(solution(10, 15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]))
print(solution(10, 21, [11, 2, 5, 6, 8, 9, 2, 3, 10, 9, 10]))
print(solution(10, 10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]))
print(solution(10, 10, [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]))
print(solution(4, 5, [1, 2, 2, 3]))
print(solution(10, 9, [1, 1, 1, 1, 1, 1, 1, 1, 1, 8]))