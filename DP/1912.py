'''
문제 : 연속합
https://www.acmicpc.net/problem/1912
'''
import sys


def solution(n: int, seq: list) -> int:
    dp = [0 for _ in range(n)]

    dp[0] = seq[0]

    for i in range(1, n):
        if dp[i-1] + seq[i] < seq[i]:
            dp[i] = seq[i]
        else:
            dp[i] = dp[i-1] + seq[i]

    return max(dp)


def main():
    input = sys.stdin.readline

    n = int(input())
    seq = list(map(int, input().split()))

    print(solution(n, seq))


if __name__ == '__main__':
    main()
