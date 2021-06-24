n = int(input())

seq = []
for _ in range(n):
    name, score = input().split()
    seq.append((name, int(score)))

answer = sorted(seq, key= lambda a:a[1])

for name, score in answer:
    print(name, end=' ')