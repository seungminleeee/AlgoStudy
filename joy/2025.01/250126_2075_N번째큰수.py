# import heapq

# N = int(input())
# heap = []

# for _ in range(N):
#     number = list(map(int, input().split()))
    
#     for num in number:
#         if len(heap) < N:
#             heapq.heappush(heap, num)
#         else:
#             if num > heap[0]:
#                 heapq.heappushpop(heap, num)

# print(heap[0])
    
import heapq

N = int(input())
heap = []

for _ in range(N):
    number = list(map(int, input().split()))

    for num in number:
        if len(heap) < N:
            heapq.heappush(heap, num)
        else:
            if heap[0] < num:
                heapq.heappushpop(heap, num)

print(heap[0])



# N = int(input())  
# numbers = []

# for _ in range(N):
#     numbers.extend(map(int, input().split()))

# numbers.sort(reverse=True)
# print(numbers[N - 1])
