n, m = map(int, input().split())
card = list(map(int, input().split()))
card.sort()
for i in range(m):
    new_num = card[0] + card[1]
    card[0] = new_num
    card[1] = new_num
    card.sort()

print(sum(card))