# 선택 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]

print('선택 정렬 : ', array)


# 삽입 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print('삽입정렬 : ', array)


# 퀵 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while (left <= right):
        # pivot보다 큰 데이터를 찾을 때까지 반복
        while (left <= end and array[left] <= array[pivot]):
            left += 1
        # pivot보다 작은 데이터를 찾을 때까지 반복
        while (right > start and array[right] >= array[pivot]):
            right -= 1

        # left와 right가 엇갈렸다면, 더 작은 값(right)을 pivot과 바꿔줌
        if (left > right):
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print('퀵 정렬 : ', array)

# 퀵 정렬2
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [a for a in tail if a <= pivot]
    right_side = [a for a in tail if a > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print('퀵 정렬2 : ', quick_sort(array))


# 두 배열의 원소 교체 문제
n, k = 5, 3

a = [1, 2, 5, 4, 3]
b = [5, 5, 6, 6, 5]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot, tail = array[0], array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

a, b = quick_sort(a), quick_sort(b)

for i in range(k):
    if a[i] < b[-1 - i]:
        a[i], b[-1 - i] = b[-1 - i], a[i]
    else:
        break

print(sum(a))