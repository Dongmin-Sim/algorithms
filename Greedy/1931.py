'''
문제 : 회의실 배정
https://www.acmicpc.net/problem/1931ㄴ
'''
import sys


def solution(n: int, meeting_list: list) -> int:
    meeting_list.sort(key=lambda x: (x[1], x[0]))

    result = 0
    prev_end = -float('inf')

    for cur_start, cur_end in meeting_list:
        if prev_end <= cur_start:
            result += 1
            prev_end = cur_end

    return result


def main():
    input = sys.stdin.readline

    n = int(input())
    meeting_list = []

    for i in range(n):
        start, end = map(int, input().split())
        meeting_list.append((start, end))

    print(solution(n, meeting_list))


if __name__ == '__main__':
    main()
