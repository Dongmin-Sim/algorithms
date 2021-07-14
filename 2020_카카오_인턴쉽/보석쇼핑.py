def gem_check(list, gem_set):
    return sum([i in list for i in gem_set]) == len(gem_set)

def solution(gems):
    gem_set = set(gems)

    answer = {}

    interval_gem = []
    end = 0

    for start in range(1, len(gems)+1):
        while len(interval_gem) < len(gems) and end < len(gems):
            interval_gem.append(gems[end])
            end += 1
        if gem_check(interval_gem, gem_set):
            answer[(start, end)] = end - start + 1
        interval_gem.pop(0)

    return answer


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))

#------------------------------------

list = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

# 리스트가 적어도 하나씩 포함하고 있는지 체크 =
print(sum([i in list for i in set(gems)]) == len(set(gems)))

print(sum([True, True, True, True, True]) == len(list))

#------------------------------------
def solution(gems):
    cates = set(gems)
    summary = dict()
    end = 0
    mn = 100000

    for start in range(len(gems)):
        # end값 올려서 조건 맞추기
        while len(summary) < len(cates)  and end < len(gems):
            if gems[end] in summary:
                summary[gems[end]] += 1
            else:
                summary[gems[end]] = 1
            end += 1
        # start값 올려서 범위 줄이기
        if len(summary) == len(cates):
            if (end - (start+1)) < mn:
                mn = (end - (start+1))
                ans = [start+1, end]
            if summary[gems[start]] == 1:
                summary.pop(gems[start], None)
            else:
                summary[gems[start]] -= 1
    return ans
