'''
누적 주차 시간이 기본시간 이하라면, 기본 요금을 청구
누적 주차 시간이 기본시간 초과라면, 기본 요금 + 초과한 시간 * 단위 요금 (올림)
fees : 기본 시간(분), 기본 요금, 단위 시간(분), 단위 요금
'''
from math import ceil

def solution(fees, records):
    answer = []
    numbers = []
    in_arr = {}
    time_arr = {}
    
    def calculator_time(start, end):
        s_time = int(start[:2]) * 60 + int(start[3:])
        e_time = int(end[:2]) * 60 + int(end[3:])
        total = e_time - s_time
        return total
    
    def calculator_fee(total):
        fee = fees[1]
        if total > fees[0]:
            fee += ceil((total - fees[0]) / fees[2]) * fees[3]
        return fee
    
    for record in records:
        time, number, inform = record.split()

        if inform == 'IN':
            if number not in numbers:
                numbers.append(number)
            in_arr[number] = time
        else:
            if number in time_arr:
                time_arr[number] += calculator_time(in_arr[number], time)
            else:
                time_arr[number] = calculator_time(in_arr[number], time)
            in_arr.pop(number)
    
    if in_arr:
        for key, value in in_arr.items():
            if key in time_arr:
                time_arr[key] += calculator_time(value, '23:59')
            else:
                time_arr[key] = calculator_time(value, '23:59')
            
    numbers.sort()
    
    for number in numbers:
        cur_time = time_arr[number]
        answer.append(calculator_fee(cur_time))
        
    
    return answer