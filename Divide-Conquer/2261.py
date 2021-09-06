'''
문제 : 가장 가까운 두점
https://www.acmicpc.net/problem/2261
'''


def getDist(point_1, point_2) -> int:
    x1, y1 = point_1
    x2, y2 = point_2
    return (x1-x2) ** 2 + (y1-y2) ** 2


def solution(points: list):
    result = float('inf')

    for i in range(len(points)-1):
        for j in range(i+1, len(points)):
            result = min(result, getDist(points[i], points[j]))
    return result


def main():
    n = int(input())
    points = []
    for _ in range(n):
        a, b = map(int, input().split())

        points.append((a, b))

    print(solution(points))


if __name__ == '__main__':
    main()
