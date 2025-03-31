n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

friend = set(graph[1]) # ㄹㅇ 친구

for i in graph[1]:
    friend.update(graph[i]) # 친구의 친구

friend.discard(1) # 나 뺌

print(len(friend))