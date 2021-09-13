'''
문제 : 암호 만들기
랭크 : 골드 5
https://www.acmicpc.net/problem/1759
'''
import sys
from itertools import combinations


# def ascending_check(n, perm):
#     '''해당 조합이 오름차순이면 True 반환, 아닐 경우 False 반환'''
#     previous_ord = -float('inf')

#     for i in range(n):
#         temp = ord(perm[i])
#         if temp > previous_ord:
#             previous_ord = temp
#         else:
#             return False

#     return True


def counting_vowels(c, n, perm):
    cnt = 0
    for i in range(n):
        if perm[i] in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1

    return cnt


def solution(l, c, password):
    '''
    1. 암호는 L개, 최소 1개의 모음(a, e, i, o, u) + 최소 2개의 자음으로 구성
    2. 알파벳 오름차순
    '''
    password.sort()
    candidate = []
    perms = list(combinations(password, l))

    for perm in perms:
        n = len(perm)

        # if not ascending_check(n, perm):
        #     continue

        if 2 <= (l - counting_vowels(c, n, perm)) < l:
            candidate.append(perm)

    return candidate


def main():
    input = sys.stdin.readline

    l, c = map(int, input().split())
    password = input().split()

    candidate = solution(l, c, password)

    for i in range(len(candidate)):
        print(''.join(candidate[i]))


if __name__ == '__main__':
    main()
