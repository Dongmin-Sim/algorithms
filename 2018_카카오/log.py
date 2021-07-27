# https://dev-note-97.tistory.com/170 코드 참고

def get_time(log):
    _, time, respond = log.split()
    hour, minute, sec = time.split(':')
    end_time = (int(hour) * 3600000) + (int(minute)
                                        * 60000) + int(sec.replace('.', ''))
    start_time = end_time - int(float(respond.replace('s', '')) * 1000) + 1

    return (start_time, end_time) if start_time > 0 else (0, end_time)


def solution(lines):
    answer = 0
    time_list = []
    for i in range(len(lines)):
        start_time, end_time = get_time(lines[i])
        time_list.append((start_time, end_time))

    for i in range(len(time_list)):
        count = 1
        i_end_time = time_list[i][1]
        for j in range(len(time_list)):
            if i == j:
                continue
            j_start_time, j_end_time = time_list[j][0], time_list[j][1]

            if i_end_time <= j_start_time and j_start_time < (i_end_time + 1000):
                count += 1
            elif i_end_time <= j_end_time and j_end_time < (i_end_time + 1000):
                count += 1
            elif j_start_time <= i_end_time and (i_end_time + 100) <= j_end_time:
                count += 1

    if count > answer:
        answer = count
    return answer


# 프로그래머스 풀기
def solution2(lines):

    # get input
    S, E = [], []
    totalLines = 0
    for line in lines:
        totalLines += 1
        type(line)
        (d, s, t) = line.split(" ")

       # time to float
        t = float(t[0:-1])
        (hh, mm, ss) = s.split(":")
        seconds = float(hh) * 3600 + float(mm) * 60 + float(ss)

        E.append(seconds + 1)
        S.append(seconds - t + 0.001)
    print(S, E)
    # count the maxTraffic
    S.sort()
    print(S, E)
    curTraffic = 0
    maxTraffic = 0
    countE = 0
    countS = 0
    while((countE < totalLines) & (countS < totalLines)):
        if(S[countS] < E[countE]):
            curTraffic += 1
            maxTraffic = max(maxTraffic, curTraffic)
            countS += 1
        else:  # it means that a line is over.
            curTraffic -= 1
            countE += 1

    return maxTraffic


# print(solution2(["2016-09-15 01:00:04.001 2.0s",
#       "2016-09-15 01:00:07.000 2s"]))
# print(solution2(["2016-09-15 01:00:04.002 2.0s",
#       "2016-09-15 01:00:07.000 2s"]))
print(solution2(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s",
      "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))
