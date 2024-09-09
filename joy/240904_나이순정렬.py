# 틀렷대... 힝.... 아놔 승민언니 말 듣고 람다로 했는데 
# x[1] 로 하고 있었어 ;;;;;;; 아놔! 

N = int(input())
lst = []
for i in range(N):
  num, name = input().split()
  lst.append((int(num), name))

lst.sort(key= lambda x: x[0])

for i in lst:
  print(i[0], i[1]) 
  
  
  