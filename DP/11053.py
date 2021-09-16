'''
문제 : 가장 긴 증가하는 부분수열
https://www.acmicpc.net/problem/11053
'''
import sys


def solution(n: int, seq: list) -> int:
    dp = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if seq[j] < seq[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def main():
    input = sys.stdin.readline
    n = int(input())
    seq = list(map(int, input().split()))

    print(solution(n, seq))


if __name__ == '__main__':
    main()
