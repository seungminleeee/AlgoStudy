import heapq

N = int(input())
heap = []

for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(N):
        if len(heap) < N:
            heapq.heappush(heap, lst[j])
        else:
            if lst[j] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, lst[j])

ans = heapq.heappop(heap)
print(ans)