from collections import deque


def cmd_trans(cmd, selected, arr):
    direction, num = cmd.split()
    num = int(num)

    idx = selected
    while True:
        if num == 0:
            break

        if direction == 'D':
            idx += 1
        else:
            idx -= 1

        if arr[idx] == 'X':
            pass
        else:
            selected = idx
            num -= 1

    return selected


def solution(n, k, cmd):
    # 초기 상태
    arr = ['O'] * n
    selected = k
    reverse = deque()

    for c in cmd:
        if c == 'C':
            arr[selected] = 'X'
            reverse.append(selected)

            if selected == n - 1:
                selected -= 1
            else:
                selected += 1

        elif c == 'Z':
            idx = reverse.pop()
            arr[idx] = 'O'

        else:
            selected = cmd_trans(c, selected, arr)

    answer = arr[0]
    for i in arr[1:]:
        answer += i
    print(selected)
    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 0, ["C", "C", "C", "C",
      "C", "C", "C", 'Z', 'Z', 'Z', 'U 1', 'C']))
print(solution(8, 2, ["D 2", "C", "U 3", "C",
      "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
