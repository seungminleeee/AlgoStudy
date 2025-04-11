"""
[BOJ] 신입 사원 / 실버1
"""
import sys
input = sys.stdin.readline

def max_find(sorted_rank):
    res = 0
    min_interview_rank = float('inf')
    for document_rank, interview_rank in sorted_rank:
        if document_rank == 1:
            min_interview_rank = interview_rank
            res += 1

        elif interview_rank > min_interview_rank:
            continue

        else:
            min_interview_rank = interview_rank
            res += 1

    return res

t = int(input())  # (1 ≤ T ≤ 20)
for _ in range(t):
    n = int(input())  # (1 ≤ N ≤ 100,000)

    ranks = []
    for _ in range(n):
        document_rank, interview_rank = map(int, input().split())
        ranks.append((document_rank, interview_rank))

    sorted_rank = sorted(ranks, key=lambda x: x[0])

    print(max_find(sorted_rank))