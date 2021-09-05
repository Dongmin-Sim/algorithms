'''
연속부분

'''

import sys
input = sys.stdin.readline

n = int(input())
l = [0] + list(map(int, input().split())) + [0]
psum = l[:]

for i in range(1, n+2):
    psum[i] += psum[i-1]

s = [0]
ans = 0
idx = (1, 1)
for i in range(1, n + 2):
    while s and l[s[-1]] > l[i]:
        minn = l[s.pop()]
        res = (psum[i - 1] - psum[s[-1]]) * minn
        print(res)
        if ans < res:
            ans = res
            idx = (s[-1] + 1, i - 1)
    s.append(i)
    print(s)
print(ans)
print(idx[0], idx[1])
