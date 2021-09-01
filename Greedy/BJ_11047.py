# https://www.acmicpc.net/problem/11047
n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

cnt = 0

for i in range(len(coins)-1, -1, -1):
    q, r = divmod(k, coins[i])
    cnt += q
    k = r


print(cnt)
