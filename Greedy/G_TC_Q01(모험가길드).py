from collections import deque
import time

n = int(input())
adventure = list(map(int, input().split()))

adventure.sort(reverse=True)

def solution(array:list):
    start = time.time()
    # deque사용
    q = deque(array)
    # 결성된 group 수
    group = 0
    # 큐가 빌때까지
    while q:
        try:
            # 내림차순 된 리스트에서 첫번째 값 반환
            start = q.popleft()
            # 첫번째 값의 수 만큼 popleft()
            for _ in range(start-1):
                q.popleft()
        # error 발생 시(공포도 만큼 팀 결성 불가) ==> 반복문 탈출
        except IndexError as e:
            break
        # 그룹 결성
        group += 1

    a_time = time.time() - start
    # 그룹 수 return
    return group, a_time


def answer(array):
    start = time.time()
    # 오름차순 정렬
    array.sort()

    # 총 그룹 수
    result = 0
    # 그룹 포함 인원 수
    count = 0

    # 반복문
    for element in array:
        # 그룹 포함 인원 수 + 1
        count += 1
        # 만약 현재
        if count >= element:
            result += 1
            count = 0

    a_time = time.time() - start
    return result, a_time

# solution의 시간복잡도가 좋지 않음
print(solution(adventure))
print(answer(adventure))

# 테스트 케이스
print(solution([1, 2, 2, 3, 3, 4]))
print(solution([2, 3, 1, 2, 2]))
print(solution([5, 5, 5, 5, 3, 3]))
