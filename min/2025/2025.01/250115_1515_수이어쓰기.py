S = input()

s = ''
check = 0
N = 1

while check < 1:
    n = str(N)
    for i in n:
        new_s = s + i
        if new_s in S[:len(new_s)]:
            s = new_s
        if s == S:
            check = 1
            break
    else:
        N += 1

print(N)