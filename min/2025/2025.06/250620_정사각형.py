def solve_d(x, y):
    d = (abs(x[0] - y[0])) ** 2 + (abs(x[1]-y[1])) ** 2
    return d

T = int(input())
for _ in range(T):
    arr = [list(map(int, input().split())) for _ in range(4)]

    ret = []
    for i in range(4):
        for j in range(i+1, 4):
            ret.append(solve_d(arr[i], arr[j]))

    ret.sort()

    if ret.count(ret[0]) == 4 and ret.count(ret[-1]) == 2:
        print(1)
    else:
        print(0)