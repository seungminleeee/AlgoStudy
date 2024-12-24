# 시간초과 ... omg 
N = int(input())
lst = []
for i in range(1, N + 1):
    lst.append(i)

while len(lst) > 1:
    lst.pop(0)
    lst.append(lst.pop(0)) # 맨 위 카드를 아래로 .. 

print(lst[0])

from collections import deque
N = int(input())
queue = deque(range(1, N + 1))

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])