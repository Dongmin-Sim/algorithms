from bisect import bisect_left, bisect_right

def solution(N, array, x):
    left = bisect_left(array, x)
    right = bisect_right(array, x)
    answer = right - left

    if answer == 0:
        return -1
    else:
        return answer


print(solution(7, [1, 1, 2, 2, 2, 2, 3], 7))
print(solution(7, [1, 1, 2, 2, 2, 2, 3], 1))
print(solution(7, [1, 1, 2, 2, 2, 2, 3], 2))
print(solution(7, [1, 1, 2, 2, 2, 2, 3], 3))

# --------------------

def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target and (mid == 0 or array[mid - 1] < target):
        return mid
    # target값과 같아도 오른쪽을 계속 줄여나감(연속된 원소중에서 제일 왼쪽을 찾기 위해)
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    else:
        return first(array, target, mid + 1, end)

def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target and (mid == len(array) - 1 or array[mid + 1] > target):
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    # target값과 같아도 왼쪽을 계속 줄여나감(연속된 원소중에서 제일 오른쪽을 찾기 위해)
    else:
        return last(array, target, mid + 1, end)


def count(n, array, x):
    left = first(array, x, 0, n-1)
    if left == None:
        return -1

    right = last(array, x, 0, n-1)

    return right - left + 1



print(count(7, [1, 1, 2, 2, 2, 2, 3], 7))
print(count(7, [1, 1, 2, 2, 2, 2, 3], 1))
print(count(7, [1, 1, 2, 2, 2, 2, 3], 2))
print(count(7, [1, 1, 2, 2, 2, 2, 3], 3))