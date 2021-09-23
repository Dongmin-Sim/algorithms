'''
문제 : 체스판 다시 칠하기
https://www.acmicpc.net/problem/1018
'''
import sys


def check(idx: bool, x: int, y: int, Map: list) -> int:
    """8*8 체스판에서 다시 칠해야하는 정사각형의 개수를 리턴하는 함수

    Args:
        idx (bool): 체스판의 좌상단 색깔
        x (int): 체스판의 좌상단 x좌표(세로)
        y (int): 체스판의 좌상단 y좌표(가로)
        Map (list): 보드 상태

    Returns:
        int: 다시 칠해야하는 정사각형의 개수
    """
    count = 0

    colors = ['W', 'B']

    for i in range(x, x + 8):
        idx = not idx

        for j in range(y, y + 8):
            if Map[i][j] != colors[idx]:
                count += 1
            # 색 변경
            idx = not idx

    return count


def solution(n: int, m: int, Map: list) -> int:
    min_count = []

    x = n - 8 + 1
    y = m - 8 + 1

    for i in range(x):
        for j in range(y):
            min_count.append(check(True, i, j, Map))
            min_count.append(check(False, i, j, Map))

    return min(min_count)


def main():
    input = sys.stdin.readline

    n, m = map(int, input().split())
    Map = []

    for i in range(n):
        Map.append(list(input()))

    print(solution(n, m, Map))


if __name__ == '__main__':
    main()
