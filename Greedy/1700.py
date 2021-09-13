'''
문제 : 멀티탭 배정
랭크 : 골드 1
https://www.acmicpc.net/problem/1700
'''
import sys
from collections import deque


def solution(n: int, k: int, application: list) -> int:
    # 멀티탭의 개수가 더 많다면 그냥 리턴
    if n >= k:
        return 0

    result = 0
    multi_tap = []

    while len(application) > 0:
        cur_app = application.pop(0)

        if cur_app in multi_tap:
            continue

        if len(multi_tap) < n:
            multi_tap.append(cur_app)
            continue

        # 콘센트 중 하나를 빼야하는 상황
        else:
            latest_idx = 0
            latest_tap = 0
            # 멀티탭에 꽆혀 있는 코드를 돌면서 가장 나중에 사용되는 코드를 제거
            for idx, tap in enumerate(multi_tap):
                # 현재 꽃혀있는 코드가 추후에 사용될 예정이 없는 경우
                if tap not in application:
                    latest_tap = idx
                    break

                temp = application.index(tap)

                if temp > latest_idx:
                    latest_idx = temp
                    latest_tap = idx

            # 해당 코드 뽑고 현재 코드 삽입
            multi_tap.pop(latest_tap)
            multi_tap.append(cur_app)
            result += 1

    return result


def main():
    input = sys.stdin.readline

    n, k = map(int, input().split())
    application = list(map(int, input().split()))

    print(solution(n, k, application))


if __name__ == '__main__':
    main()
