def move(matrix, top, left, bottom, right):
    temp = matrix[top][left]
    min_value = temp

    # 왼쪽
    for x in range(top, bottom):
        val = matrix[x+1][left]
        matrix[x][left] = val

        min_value = min(min_value, val)

    # 하단
    for y in range(left, right):
        val = matrix[bottom][y+1]
        matrix[bottom][y] = val

        min_value = min(min_value, val)

    # 오른쪽
    for x in range(bottom, top, -1):
        val = matrix[x-1][right]
        matrix[x][right] = val

        min_value = min(min_value, val)

    # 상단
    for y in range(right, left, -1):
        val = matrix[top][y-1]
        matrix[top][y] = val

        min_value = min(min_value, val)

    matrix[top][left+1] = temp
    return min_value


def solution(rows, columns, queries):
    answer = []
    matrix = []

    num = 1
    for i in range(rows):
        row = [i for i in range(num, num+columns)]
        matrix.append(row)
        num += columns

    for x1, y1, x2, y2 in queries:
        answer.append(move(matrix, x1-1, y1-1, x2-1, y2-1))

    return answer
