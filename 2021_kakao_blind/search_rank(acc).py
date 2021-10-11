def search(candidate, query):

    cnt = list(range(len(candidate)))

    for idx, info in enumerate(query):
        temp = []

        if idx < 4:
            for c in cnt:
                # 지원자의 조건과 쿼리 조건이 일치할 경우
                if candidate[c][idx] == info:
                    temp.append(c)
                # 쿼리 조건이 '-'일 경우
                if info == '-':
                    temp.append(c)

            cnt = temp
        else:
            for c in cnt:
                if int(candidate[c][idx]) >= int(info):
                    temp.append(c)
            cnt = temp

    return len(cnt)


def solution(infos, queries):
    answer = []

    # 후보자등록
    candidate = {}

    for idx, info in enumerate(infos):
        candidate[int(idx)] = info.split()

    # 질의문
    transQueries = []

    for query in queries:
        temp = query.split()

        for t in temp:
            if t == 'and':
                temp.remove('and')
        transQueries.append(temp)

    # 조건 검색
    for query in transQueries:
        answer.append(search(candidate, query))

    return answer
