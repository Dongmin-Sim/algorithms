import sys
input = sys.stdin.readline

N = int(input())

card_array = list(map(int, input().split()))
card_array.sort()

def left(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target and (array[mid - 1] < target or mid == 0):
        return mid
    elif array[mid] >= target:
        return left(array, target, start, mid - 1)
    else:
        return left(array, target, mid + 1, end)

def right(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # if (target < array[mid + 1] or mid == len(array) - 1) and array[mid] == target: # 오류남..
    if array[mid] == target and (mid == len(array) - 1 or target < array[mid + 1]):
        return mid
    elif array[mid] > target:
        return right(array, target, start, mid - 1)
    else:
        return right(array, target, mid + 1, end)

def count(array, target, n):
    a = left(array, target, 0, n-1)

    if a == None:
        return 0

    b = right(array, target, 0, n-1)

    return b - a + 1

check_num = int(input())
check_list = list(map(int, input().split()))

for card in check_list:
    print(count(card_array, card, N), end=' ')



