# 1학기때 프로그래머스에서 풀었던 유형인듯..!
# 다리를 덱으로 구현 ( popleft : 다리 빠져나옴, append : 다리에 트럭 올리기 또는 빈 도로 올리기 )

from collections import deque

n, w, L = map(int, input().split())  # 트럭 수, 다리 길이, 최대 하중
trucks = list(map(int, input().split()))

bridge = deque([0] * w)
bridge_weight = 0
i = 0
result = 0

while bridge:

    # 다리 하나 이동
    out = bridge.popleft()
    bridge_weight -= out

    # 트럭 올리기
    # 아직 안올라간 트럭 있고, 최대 하중을 넘지 않으면 트럭 올리기
    if i <= n-1 and bridge_weight + trucks[i] <= L:
        bridge.append(trucks[i])
        bridge_weight += trucks[i]
        i += 1
    elif i <= n-1:
        bridge.append(0)

    # 시간 흐름
    result += 1

print(result)