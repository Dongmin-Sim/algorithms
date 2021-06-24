# 시간초과
n = int(input())
seq = list(map(int, input().split()))

antena = []

for i in range(1, max(seq) + 1):
    dist = 0
    for a in seq:
        dist += abs(i - a)
    antena.append((i, dist))

antena.sort(key=lambda x:x[1])

print(antena[0][0])

'''
중간값에 해당하는 위치의 집에 안테나를 설치했을 때, 안테나로부터 모든 집까지의 거리가 거리의 총합이 최소가 됨.
주어지는 집의 위치가 인덱스의 위치와 동일하기 때문에 어떤 경우든 중앙값이 최소거리를 보장함.
리스트 정렬 -> 인덱스 중앙값에 해당하는 값 출력
'''
n = int(input())
seq = list(map(int, input().split()))

seq.sort()

print(seq[n-1 // 2])