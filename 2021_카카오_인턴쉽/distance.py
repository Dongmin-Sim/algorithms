from collections import deque


def manhattan_dist(x1, x2, y1, y2):
    return abs(x1-x2) + abs(y1 - y2)


def find_p(places):
    loc = []
    for i in range(5):
        for j in range(5):
            if places[i][j] == 'P':
                loc.append((i, j))
    return loc


def bfs(init_x, init_y, place):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[0] * 5 for _ in range(5)]

    que = deque()
    que.append((init_x, init_y))

    while que:
        x, y = que.popleft()
        # print('x, y : ', x, y)
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue

            if place[nx][ny] == 'X':
                continue

            if visited[nx][ny] == 0 and place[nx][ny] != 'P':
                visited[nx][ny] = 1  #
                que.append((nx, ny))

            if place[nx][ny] == 'P' and visited[nx][ny] == 0:
                if manhattan_dist(init_x, nx, init_y, ny) <= 2:
                    print(visited, (nx, ny))
                    return 0
                else:
                    return 1
    print(visited)
    return 1


def solution(places):
    answer = []
    places = deque(places)

    while places:
        result = 1

        place = places.popleft()
        # 모든 p의 위치
        p_loc = find_p(place)
        print('p위치 : ', len(p_loc))
        # p 가 없다면 skip
        if len(p_loc) == 0:
            answer.append(1)
            continue

        # 각 p의 위치마다 bfs
        for loc in p_loc:

            a = bfs(loc[0], loc[1], place)
            print(loc, a)
            result *= a

        if result == 0:
            answer.append(0)
        else:
            answer.append(1)

    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
          ['OOOOO', 'OOOOO', 'OOOOO', 'OOOOO', 'OOOOO'],
          ['XXXXX', 'XXXXX', 'XXXXX', 'XXXXX', 'XXXXX']
          ]

answer = solution(places)
print(answer)
