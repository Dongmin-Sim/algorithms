def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i, n in enumerate(prices):
        while stack and n < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
    return answer