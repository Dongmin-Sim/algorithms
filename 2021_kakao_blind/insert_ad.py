def convert(time):
    h, m, s = time.split(":")
    return (int(h) * 60 * 60) + (int(m) * 60) + int(s)


def solution(play_time, adv_time, logs):
    # 영상시간 초 환산
    play_time_sec = convert(play_time)

    # 광고시간 초 환산
    adv_time_sec = convert(adv_time)

    total_time = [0 for _ in range(play_time_sec + 1)]

    # 로그시간 초 환산
    for log in logs:
        start_log, end_log = log.split("-")
        start_log = convert(start_log)
        end_log = convert(end_log)

        total_time[start_log] += 1
        total_time[end_log] -= 1

    for i in range(1, play_time_sec):
        total_time[i] = total_time[i] + total_time[i-1]

    cur_sum = sum(total_time[:adv_time_sec])

    max_sum = cur_sum
    max_idx = 0

    for i in range(adv_time_sec, play_time_sec):
        cur_sum = cur_sum + total_time[i] - total_time[i-adv_time_sec]
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_idx = i - adv_time_sec + 1

    answer = '%02d:%02d:%02d' % (max_idx/3600, max_idx/60 % 60, max_idx % 60)

    return answer
