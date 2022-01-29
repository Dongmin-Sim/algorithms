import collections

def solution(clothes):
    answer = collections.defaultdict(int)
    
    for c in clothes:
        answer[c[1]] += 1
    
    cnt = 1
    for i in answer.values():
        cnt *= (i+1)
        
    return cnt - 1