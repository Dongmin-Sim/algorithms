'''
리팩토링 
1. parent_child 정의시 zip 함수로 리팩토링
2. cal_money 재귀함수로 변경
'''


def cal_money(seller, amount):
    global parent_child

    if seller == '-' or amount < 0:
        return

    if amount < 1:
        parent_child[seller][1] += amount
        next_profit = 0
    else:
        next_profit = int(amount * 0.1)
        parent_child[seller][1] += amount - next_profit

    cal_money(parent_child[seller][0], next_profit)


def solution(enroll, referral, seller, amount):
    global parent_child

    parent_child = {}
    for e, r in zip(enroll, referral):
        parent_child[e] = [r, 0]

    for s, a in zip(seller, amount):
        cal_money(s, a*100)

    return [values[1] for _, values in parent_child.items()]


enroll, referral, seller, amount = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], [
    "-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]


print(solution(enroll, referral, seller, amount))
