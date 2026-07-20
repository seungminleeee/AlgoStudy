A, B = map(int, input().split())

arr = []
k = 1
while k<A+B:
    for i in range(k):
        arr.append(k)
    k += 1
    if k >= A+B+1:
        break

sm = 0
for j in range(A-1, B):
    sm += arr[j]

print(sm)