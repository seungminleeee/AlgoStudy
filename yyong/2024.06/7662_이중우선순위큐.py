# 파이파이 301440 KB, 3748 ms

from heapq import heappop, heappush

for _ in range(int(input())):
    k = int(input())
    not_removed = {}  # 원래 리스트로 저장했는데 시간초과 나서 질문게시판 보고 딕셔너리 형태로 바꿈..
    minQ = []
    maxQ = []
    

    for i in range(k):
        case, num = map(str, input().split()) # 작업 종류, 숫자
        
        if case == 'I':
            heappush(minQ, int(num))          # 최소 그대로 저장
            heappush(maxQ, int(num) * (-1))   # 최대는 반대로 저장

            if int(num) in not_removed:       # 중복숫자 있으면
                not_removed[int(num)] += 1    # 추가
            else:
                not_removed[int(num)] = 1     # 아니면 새로 저장
            

        elif case == 'D' and not_removed:     # 지워야하고 아직 숫자 남아있으면

            if num == '-1':                   # 최솟값 삭제

                while minQ:
                    cur_num = heappop(minQ)

                    if cur_num in not_removed:
                        not_removed[cur_num] -= 1

                        if not_removed[cur_num] == 0:
                            not_removed.pop(cur_num)
                        break
                    
            else:                              # 최댓값 삭제
                while maxQ:
                    cur_num = heappop(maxQ)

                    if cur_num * (-1) in not_removed:
                        not_removed[cur_num * (-1)] -= 1

                        if not_removed[cur_num * (-1)] == 0:
                            not_removed.pop(cur_num * (-1))
                        break
        
        # print(minQ)
        # print(maxQ)
        # print(not_removed)


    if not_removed:

        while True:   # 최소에서 지운 값 찾아서 지우기
            max_num = heappop(maxQ)
            if max_num * (-1) in not_removed:
                break

        while True:   # 최대에서 지운 값 찾아서 지우기
            min_num = heappop(minQ)
            if min_num in not_removed:
                break

        print(max_num * (-1), min_num)
    
    else:
        print('EMPTY')