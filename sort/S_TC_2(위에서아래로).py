n = int(input())

seq = [int(input()) for _ in range(n)]

answer = sorted(seq, reverse=True)

for a in answer:
    print(a, end=' ')