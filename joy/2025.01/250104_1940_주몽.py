N = int(input())
M = int(input())
arr = list(map(int, input().split()))
rev_arr = sorted(arr, reverse=True)
cnt = 0

while rev_arr:
    num = rev_arr.pop(0)
    print(num)
    print(rev_arr)
    for i in rev_arr:
        if num + i == M:
            cnt += 1
            rev_arr.remove(i)
            break
        elif num + i > M:
            continue
        else:
            break

print(cnt)
