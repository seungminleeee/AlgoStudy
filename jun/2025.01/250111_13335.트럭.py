"""
[BOJ] 13335번: 트럭 / 실버1

조건:
1. 시간 제한 1초
2. n개의 트럭, 순서 바꾸기 X, 다리 위에는 w대의 트럭만 동시에 가능
3. 트럭의 무게의 합은 L보다 작거나 같다.
4. 1 <= n <= 1,000 / 1 <= w <= 100 / 10 <= L <= 1,000

생각:
1. 예전에 이런거 스터디 할때 풀어봤던 문제같음.
2. 트럭 지나가는거 큐로 만들어서 구현(앞에서 빼고 뒤에서 넣고) 때리면 될 듯.
3. 큐만 쓰게되면 시간 복잡도는 O(n)
"""
from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = deque([0] * w)
ans = 0
weight = 0

for truck in trucks:
    while True:
        ans += 1
        weight -= bridge.popleft()

        if weight + truck <= L:
            bridge.append(truck)
            weight += truck
            break
        else:
            bridge.append(0)

ans += w
print(ans)