# https://www.acmicpc.net/problem/1931
def reserveMeetingRoom(meetings: list) -> int:
    meetings.sort(key=lambda x: (x[1], x[0]))

    prev_end = 0

    result = 0

    for i in range(len(meetings)):
        cur_start, cur_end = meetings[i][0], meetings[i][1]

        if prev_end > cur_start:
            continue
        elif prev_end <= cur_start:
            result += 1
            prev_end = cur_end

    return result


def main():
    n = int(input())

    meetings = []

    for _ in range(n):
        start, end = map(int, input().split())
        meetings.append((start, end))

    print(reserveMeetingRoom(meetings))


if __name__ == '__main__':
    main()
