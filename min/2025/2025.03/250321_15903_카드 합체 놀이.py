import sys
input = sys.stdin.readline

def game(arr):
    arr.sort()
    sm = arr[0] + arr[1]
    arr[0], arr[1] = sm, sm
    return arr

N, M = map(int, input().strip().split())
cards = list(map(int, input().strip().split()))

for i in range(M):
    cards = game(cards)

print(sum(cards))
