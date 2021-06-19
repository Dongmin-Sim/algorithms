import sys
input = sys.stdin.readline

n, s = map(int, input().split())
order = list(map(int, input().split()))

def solution(n,s, order):
    # order.sort() 정렬 x

    # 부분합, 정답길이, end
    interval_sum, answer, end = 0, 0, 0

    # 투포인터 시행
    for start in range(n):
        # 부분합이 s보다 작거나, 배열 길이보다 작거나 같을때
        while interval_sum < s and end <= n:
            # 만약 end가 n과 같아지면, end + 1 한 후 반복문 탈출(index 에러방지)
            if end == n:
                end += 1
                break
            # 부분합에 현재 end 위치의 값 더하기
            interval_sum += order[end]
            # end값 늘려주기
            end += 1

        # 부분합의 길이
        length = end - start

        # 부분합이 s보다 크거나 같다면
        if interval_sum >= s:
            # answer가 0이거나, length가 answer보다 더 작으면 answer 갱신
            if answer == 0 or answer > length:
                answer = length
        # 부분합에서 start 위치의 값 빼기
        interval_sum -= order[start]

    # answer 리턴
    return answer

print(solution(n, s, order))

# 테스트 케이스
# print(solution(10, 15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]))
# print(solution(10, 21, [11, 2, 5, 6, 8, 9, 2, 3, 10, 9, 10]))
# print(solution(10, 10, [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]))
# print(solution(10, 10, [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]))
# print(solution(4, 5, [1, 2, 2, 3]))
# print(solution(10, 9, [1, 1, 1, 1, 1, 1, 1, 1, 1, 8]))


