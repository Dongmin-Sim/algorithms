'''
문제 : 약수 구하기
출처 : https://www.acmicpc.net/problem/2501
카테고리 : math
'''

def solution(N:int, K:int) -> int:
    nums = []
    for i in range(1, N+1):
        if not (N % i):
            nums.append(i)

    if len(nums) < K:
        return 0
    else:
        return nums[K-1]

    

if __name__ == "__main__":
    N, K = map(int, input().split())

    print(solution(N, K))