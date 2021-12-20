'''
문제 : 정수 삼각형
출처 : https://www.acmicpc.net/problem/1932
카테고리 : #dp
'''

def dp(n:int, tree:list):

    dp = [[0 for _ in range(i)] for i in range(1, n+1)]

    dp[0][0] = tree[0][0]

    for i in range(1, n):
        for j in range(i+1):
            if (j - 1) < 0:
                dp[i][j] = tree[i][j] + dp[i-1][j]
            elif i == j:
                dp[i][j] = tree[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = tree[i][j] + max(dp[i-1][j-1], dp[i-1][j])
                
    return max(dp[-1])


if __name__ == "__main__":
    n = int(input())

    tree = []

    for _ in range(n):
        tree.append(list(map(int, input().split())))

    print(dp(n, tree))


