light = list(input())
switch = 0
for i in range(len(light)):
    if light[i] == 'Y':
        switch += 1
        # i 배수인거 다 바꿔줌
        for j in range(i, len(light), i + 1):
            if light[j] == 'N':
                light[j] = 'Y'
            else:
                light[j] = 'N'

print(switch)