'''
문제 : 문자열 뒤집기
출처 : 리트코드
'''


def reverseString(s: list[str]) -> None:
    start, end = 0, len(s) - 1
    while start < end:
        s[end], s[start] = s[start], s[end]
        start += 1
        end -= 1


def reverse_method(s: list[str]) -> None:
    # more pythonic
    s.reverse()


if __name__ == '__main__':
    string = list(input())
    print(string)
    reverseString(string)
    print(string)