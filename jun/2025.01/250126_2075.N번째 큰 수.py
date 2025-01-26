"""
[BOJ] 2075번: N번째 큰 수 / 실3

조건:
1. 시간 제한 1초
2. 모든 수는 자신의 한 칸 위에 있는 수보다 크다.
3. 1 <= n <= 1,500

풀이:
1. for문 돌면서 힙에 넣기
2. n번 째 구하기 위해 힙 크기 n으로 제한

* 첨에 이중 for문 하다가 메모리초과 받으면서 하는걸로 바꿈

시간 복잡도 : for문 n^2, 힙 연산 log n => O(n^2 * log n) 예상
"""
import heapq

n = int(input())
heap = []
for _ in range(n):
        row = list(map(int, input().split()))
        for i in row:
            heapq.heappush(heap, i)
            if len(heap) > n:
                heapq.heappop(heap)
print(heap[0])