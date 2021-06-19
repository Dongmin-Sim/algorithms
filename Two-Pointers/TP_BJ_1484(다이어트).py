# 다이어트
# G = weight^2 - memory^2

# import sys
# input = sys.stdin.readline


g = int(input())
w = [x for x in range(1, 100001)]
N = 100000
left, right = 0, 0

ans=[]

while left < N and right < N:
    weight = (w[left] + w[right]) * (w[left] - w[right])

    if weight == g:
        ans.append(w[left])
    if weight < g:
        left += 1
    else:
        right += 1

if not ans:
    print(-1)
else:
    for x in ans:
        print(x)


