T = int(input())
for _ in range(T):
    N = int(input())
    pig = list(map(int, input().split()))
    meal = pig.copy()

    day = 1
    while sum(meal) <= N:
        for i in range(6):
            if i == 0:
                meal[0] = meal[0] + pig[1] + pig[5] + pig[3]
            elif i == 5:
                meal[5] = meal[5] + pig[0] + pig[4] + pig[2]
            else:
                meal[i] = meal[i] + pig[i-1] + pig[i+1] + pig[(i+3)%6]

        for i in range(6):
            pig[i] = meal[i]
        day += 1

    print(day)