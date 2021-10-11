from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for c in course:
        temp = []
        for order in orders:
            temp += combinations(sorted(order), c)

        if temp:
            orderCount = Counter(temp)

            max_ = max(orderCount.values())

            if max_ >= 2:
                for key, value in orderCount.items():
                    if orderCount[key] == max_:
                        answer.append(''.join(key))

    answer.sort()

    return answer
