"""
[BOJ] 21939번: 문제 추천 시스템 Version 1 / 골드4
"""
import heapq

n = int(input())

# 최소 정렬
min_heap = []
# 최대 정렬
max_heap = []
# 문제 저장
problems = {}
# 해결 목록
solved = set()

for _ in range(n):
    p, l = map(int, input().split())
    # 난이도 순으로 정렬
    heapq.heappush(min_heap, (l, p))
    heapq.heappush(max_heap, (-l, -p))
    # 문제 저장
    problems[p] = l

m = int(input())
for _ in range(m):
    command = input().split()

    if command[0] == 'recommend':
        x = int(command[1])
        if x == 1:
            while max_heap:
                l, p = max_heap[0]
                l, p = -l, -p
                # 해결 안됐고, 문제 일치 확인
                if p not in solved and problems[p] == l:
                    print(p)
                    break
                heapq.heappop(max_heap)

        else:
            while min_heap:
                l, p = min_heap[0]
                # 해결 안됐고, 문제 일치 확인
                if p not in solved and problems[p] == l:
                    print(p)
                    break
                heapq.heappop(min_heap)

    # 문제 추가
    elif command[0] == 'add':
        p, l = int(command[1]), int(command[2])
        heapq.heappush(min_heap, (l, p))
        heapq.heappush(max_heap, (-l, -p))
        problems[p] = l
        # 기존 삭제된 문제인데 다시 추가될 경우
        if p in solved:
            solved.remove(p)

    # 문제 해결 (solved)
    else:
        p = int(command[1])
        solved.add(p)



# 시간 초과 ver (그냥 구현)
# --------------------------------------------------------------
# def recommend(x):
#     problems.sort(key=lambda x: (-x[1], -x[0]))
#     # x가 1인 경우 추천 문제 리스트에서 가장 어려운 문제의 번호를 출력한다.
#     # 만약 가장 어려운 문제가 여러 개라면 문제 번호가 큰 것으로 출력한다.
#     if x == 1: return problems[0][0]
#     # x가 -1인 경우 추천 문제 리스트에서 가장 쉬운 문제의 번호를 출력한다.
#     # 만약 가장 쉬운 문제가 여러 개라면 문제 번호가 작은 것으로 출력한다.
#     elif x == -1: return problems[-1][0]
#
# def add(p, l):
#     # 	추천 문제 리스트에 난이도가 L인 문제 번호 P를 추가한다.
#     problems.append((p, l))
#
# def solved(p):
#     # 추천 문제 리스트에서 문제 번호 P를 제거한다.
#     find_idx = 0
#     for idx, (a, b) in enumerate(problems):
#         if a == p:
#             find_idx = idx
#     problems.pop(find_idx)
#
# n = int(input())  # 1 <= n, p <= 100,000
#
# problems = []
# for _ in range(n):
#     p, l = map(int, input().split())  # 1 <= l <= 100
#     problems.append((p, l))
#
# m = int(input())
# for _ in range(m):  # 1 <= m <= 10,000
#     command = list(map(str, input().split()))
#
#     # recommend x
#     if command[0] == 'recommend':
#         # recommend 명령이 주어질 때마다 문제 번호를 한 줄씩 출력한다.
#         print(recommend(int(command[1])))
#
#     # add p l
#     elif command[0] == 'add':
#         add(int(command[1]), int(command[2]))
#
#     # solved p
#     elif command[0] == 'solved':
#         solved(int(command[1]))