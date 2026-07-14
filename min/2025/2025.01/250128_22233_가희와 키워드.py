import sys
sys.stdin=open('input.txt')
input = sys.stdin.readline

N, M = map(int,input().split())
memo = set(input().rstrip() for _ in range(N))

for i in range(M):
    words = set(map(str, input().strip().split(',')))
    memo -= words
    print(len(memo))