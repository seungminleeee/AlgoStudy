from itertools import permutations

n = int(input())
k = int(input())
num = []
for i in range(n):
  num.append(input())
  
arr = list(permutations(num, k))

# 순열에서 중복된 부분을 제거해줘야한다! 중복되지 말라 했으니께~~ 
arr1 = set() 

for i in arr:
  arr1.add(''.join(i))

print(len(arr1))
