'''
문제 : 히스토그램
https://www.acmicpc.net/problem/1725
'''


def solution(bins):
    n = len(bins)

    if n <= 1:
        return bins[0]

    mid = n // 2

    # mid를 기준으로 왼쪽 오른쪽  구간의 직사각형 최대 넓이 값
    left = solution(bins[:mid])
    right = solution(bins[mid:])

    # 중간 mid 값을 걸치는 경우의 직사각형 최대 넓이 값
    mid_leftPtr = mid - 1
    mid_rightPtr = mid

    minHeight = min(bins[mid_leftPtr], bins[mid_rightPtr])
    curArea = minHeight * 2

    while mid_leftPtr - 1 >= 0 or mid_rightPtr + 1 < n:
        leftHeight = bins[mid_leftPtr - 1] if mid_leftPtr - \
            1 >= 0 else -float('inf')
        rightHeight = bins[mid_rightPtr +
                           1] if mid_rightPtr + 1 < n else -float('inf')

        if leftHeight >= rightHeight:
            mid_leftPtr -= 1
            minHeight = min(minHeight, leftHeight)
        else:
            mid_rightPtr += 1
            minHeight = min(minHeight, rightHeight)

        curArea = max(curArea, minHeight * (mid_rightPtr - mid_leftPtr + 1))

    return max(left, right, curArea)


def main():
    n = int(input())
    bins = [int(input()) for _ in range(n)]

    print(solution(bins))


if __name__ == '__main__':
    main()
