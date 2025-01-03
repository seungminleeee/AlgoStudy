# 실4 2870번 수학숙제
N = int(input())
arr = []
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
result = []
for i in range(N):
    arr.append(input())

for i in arr:
    num = ''
    for j in i:
        if j in number:
            num += j
        elif num != '': 
            result.append(int(num))
            num = ''
    if num != '':
        result.append(int(num))

result.sort()

for i in result:
    print(i)
            

   