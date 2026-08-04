from collections import defaultdict
import math

def find_time(T):
    h, m = map(int, T.split(":"))
    return h*60 + m

def find_pay(lst, time):
    # 기본시간, 기본요금, 단위시간, 단위요금
    dt, dp, ut, up = lst
    pay = 0
    pay += dp
    time -= dt
    
    if time > 0:
        pay += math.ceil(time / ut) * up
    
    return pay

def solution(fees, records):
    records_dict = defaultdict(list)
    time_dict = defaultdict(int)
    
    for record in records:
        time, num, act = record.split()
        if act == 'IN':
            records_dict[num].append(time)
        else:
            I = records_dict[num].pop()
            time_diff = find_time(time) - find_time(I)
            time_dict[num] += time_diff
    
    for num in records_dict:
        if records_dict[num]:
            I = records_dict[num].pop()
            time_diff = find_time("23:59") - find_time(I)
            time_dict[num] += time_diff
    
    pay_dict = defaultdict(int)
    for num in time_dict:
        pay_dict[num] = find_pay(fees, time_dict[num])
    
    return [pay_dict[num] for num in sorted(pay_dict)]