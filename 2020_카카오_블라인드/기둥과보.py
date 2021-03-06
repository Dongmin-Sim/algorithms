def simulation_pass(result):
    for x, y, a in result:
        if not a:  # 기둥일 경우
            if not y or (x-1, y, 1) in result or (x, y, 1) in result or (x, y-1, 0) in result:
                continue
            else:
                return False
        else:  # 보일 경우
            if (x, y-1, 0) in result or (x+1, y-1, 0) in result or ((x-1, y, 1) in result and (x+1, y, 1) in result):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    result = set()

    for x, y, a, b in build_frame:
        if b:
            result.add((x, y, a))
            if not simulation_pass(result):
                result.remove((x, y, a))
        else:
            result.remove((x, y, a))
            if not simulation_pass(result):
                result.add((x, y, a))

    # 최종구조물 상태 정렬
    answer = map(list, result)

    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))


print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [
      5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))

print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [
      1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
