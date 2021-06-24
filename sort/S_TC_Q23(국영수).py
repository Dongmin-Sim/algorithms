n = int(input())

seq = []
for _ in range(n):
    name, kor, eng, math = input().split()
    seq.append((name, int(kor), int(eng), int(math)))

seq.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for a in seq:
    print(a[0])
