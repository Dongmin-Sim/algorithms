'''
문제 : 큰 수의 법칙
출처 : 2019 국가 교육기관 코딩 테스트 
카테고리 : #greedy
'''
n, m, k = map(int, input().split())
array = list(map(int, input().split()))

# n, m, k = 5, 8, 3
# array = [2, 4, 5, 4, 6]

array.sort(reverse=True)
max1, max2 = array[0], array[1]

result = 0

while True:
    for _ in range(k):
        if m == 0:
            break
        result += max1
        m -= 1
    if m == 0:
        break
    result += max2
    m -= 1

print(result)
