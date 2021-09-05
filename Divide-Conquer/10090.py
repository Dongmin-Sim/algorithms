'''
문제 : Counting Inverions
https://www.acmicpc.net/problem/10090
'''
import sys


def countInversion(seq: list, start: int, end: int) -> tuple:
    # 기저조건 (base condition)
    if (end - start) <= 1:  # 리스트의 값이 하나라는 뜻 5- 4 5 5= 0
        return ([seq[start]], 0)  # (정렬된 리스트, 인버전 카운팅 수)

    mid = (start + end) // 2

    left_seq, num_left = countInversion(seq, start, mid)
    right_seq, num_right = countInversion(seq, mid, end)

    result_seq = []
    result_num = num_left + num_right

    i, j = 0, 0
    while i < len(left_seq) and j < len(right_seq):
        if left_seq[i] <= right_seq[j]:
            result_seq.append(left_seq[i])
            i += 1
        else:
            result_seq.append(right_seq[j])
            j += 1
            result_num += (len(left_seq) - i)  # i번째를 포함하여 뒤까지의 개수

    if i >= len(left_seq):
        result_seq += right_seq[j:]
    elif j >= len(right_seq):
        result_seq += left_seq[i:]

    return result_seq, result_num


def main():
    input = sys.stdin.readline
    n = int(input())
    seq = list(map(int, input().split()))

    _, result_num = countInversion(seq, 0, n)

    print(result_num)


if __name__ == '__main__':
    main()
