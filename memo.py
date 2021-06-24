# 선택 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)


# 삽입 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)

# 퀵 정렬(파이썬 리스트, 컴프리핸션 사용)
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [a for a in tail if a <= pivot]
    right_side = [a for a in tail if a > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort_basic(array, start, end):
    if start >= end:
        return

    pivot = array[0]
    left, right = start + 1, end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right >= start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort_basic(array, start, right - 1)
    quick_sort_basic(array, right + 1, end)

# quick_sort_basic(array, 0, len(array) - 1)
# print(array)


#----
print('hello')
n = 8
k = 3
ans = [7, 9, 7, 30, 2, 7, 9, 25]
for i in range(n-1, -k, -1):
    print(i, ans[i])

seq = [(1, 2, 3), (4, 5, 6), (1, 1, 2)]

seq.sort(key=lambda x: (-x[1], x[2], x[0]))
print(seq)


seq = [1, 2, 3, 4, 5, 6, 7]
