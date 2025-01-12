# N = int(input())
# arr = list(map(int, input().split()))
# fruit = set(arr)
# while len(fruit) > 2:
#     if len(fruit) <= 2:
#         print(len(arr))
#     else:
#         arr.pop(0)
#         fruit = set(arr)
   
# print(len(arr))       

N = int(input())
arr = list(map(int, input().split()))
fruit = {}
L = 0
max_fruit = 0
for i in arr:
    if i in fruit:
        fruit[i] += 1
    else:
        fruit[i] = 1



