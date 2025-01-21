N = int(input())
num = {}
for i in range(N):
    number = int(input())
    if number in num:
        num[number] += 1
    else:
        num[number] = 1

max_card = max((num.values()))
sort_num = sorted(num.items())

card = 0
for i in sort_num:
    if i[1] == max_card:
        card = i[0]
        break

print(card) 

