'''
문제 : 빗물
출처 : https://www.acmicpc.net/problem/14719
카테고리 : #simulation
'''
def solution(block):
    stack = []
    volumn = 0

    for i in range(len(block)):
        while stack and block[i] > block[stack[-1]]:
            top = stack.pop()

            if not len(stack):
                break

            dis = i - stack[-1] - 1 
            water = min(block[i], block[stack[-1]]) - block[top]

            volumn += (dis * water)

        stack.append(i)

    return volumn


if __name__ == "__main__":
    h, w = map(int, input().split())
    block = list(map(int, input().split()))

    print(solution(block))