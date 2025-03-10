N = int(input())
arr = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    string = input()
    for j in range(1, N + 1):
        if string[j - 1] == 'Y':
            arr[i].append(j)

result = 0
for i in range(1, N + 1):
    friend = set(arr[i]) # 1친구

    for twofriend in arr[i]:
        friend.update(arr[twofriend]) # 친구의 친구 넣어줌
    
    friend.discard(i) # 자기자신 뺌 

    result = max(result, len(friend))

print(result)

