from collections import defaultdict
from itertools import combinations, permutations
from bisect import bisect_left


def solution(infos, queries):
    '''
    지원자의 조건을 나올 수 있는 모든 경우의 수를 조합으로 구하여 dict에 저장 후,
    해당 조건에 맞는 질의문(dict_key)에 해당하는 지원자들의 점수 배열(dict_val)에서
    이진탐색을 통해 조건 점수 이상의 지원자들의 수를 리턴
    '''
    answer = []
    candict = defaultdict(list)

    # 지원자 정보
    for info in infos:
        temp = info.split()
        candiInfo, score = temp[:-1], int(temp[-1])

        # "java backend junior pizza"에 대해 0~4까지의 조합을 구함.
        # ["", "java", "backend", ..., "javabackend", "javajunior", ...]
        for i in range(0, 5):
            combi = combinations(candiInfo, i)
            # 나올 수 있는 모든 조합에 대해 지원자의 점수를 추가
            # {"":[80, 50, 150, 220], "java":[50], "backend":[50, 150], ...}
            for c in combi:
                candict[''.join(c)].append(score)

    # 지원자 점수 오름차순 정렬
    for key in candict:
        candict[key].sort()

    # 문의 조건
    for query in queries:
        temp = query.split()
        query, score = temp[:-1], int(temp[-1])

        # 전처리
        while "and" in query:
            query.remove("and")
        while "-" in query:
            query.remove("-")
        query = ''.join(query)

        # 만약 쿼리가 지원자 정보 딕셔너리에 있다면
        if query in candict:
            candidates = candict[query]
            # 요구점수 이상인 지원자들의 수
            count = len(candidates) - bisect_left(candidates, score)
            answer.append(count)
        # 없다면 0
        else:
            answer.append(0)

    return answer
