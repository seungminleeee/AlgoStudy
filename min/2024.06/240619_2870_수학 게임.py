# 메모리 31120 시간 40

T = int(input())

arr = []
for tc in range(T):
    item = str(input())
    N = len(item)

    nitem = item + '-'

    lst = []
    num = ''
    for i in range(0, N+1):
        if nitem[i].isdigit():
            num += nitem[i]
        else:
            lst.append(num)
            num = ''

    for j in lst:
        if j.isdigit():
            arr.append(int(j))

arr.sort()
for n in arr:
    print(n)