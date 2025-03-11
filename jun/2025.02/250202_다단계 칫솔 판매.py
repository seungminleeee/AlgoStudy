"""
[PGS] 다단계 칫솔 판매 / LV3
"""
def solution(enroll, referral, seller, amount):
    people = {enroll[i]: referral[i] for i in range(len(enroll))}
    profit = {name: 0 for name in enroll}

    for i in range(len(seller)):
        man = seller[i]
        money = amount[i] * 100

        while man != "-" and money > 0:
            send = money // 10
            keep = money - send
            profit[man] += keep
            man = people[man]
            money = send

    return [profit[name] for name in enroll]