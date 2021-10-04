def solution(lottos, win_nums):
    answer = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    corr = 0
    magic_num = 0

    for lotto in lottos:
        if not lotto:
            magic_num += 1
            continue
        if lotto in win_nums:
            corr += 1

    if corr > 0:
        min_rate = corr
        max_rate = corr + magic_num
    else:
        min_rate = corr
        max_rate = corr + magic_num

    return list(answer[max_rate], answer[min_rate])
