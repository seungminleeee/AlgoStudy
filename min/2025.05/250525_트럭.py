N, W, L = map(int, input().split())
trucks = list(map(int, input().split()))

bridge = [0]*W

idx = 0
time = 0

while len(bridge) > 0:
    time += 1
    bridge.pop(0)

    if idx < N and sum(bridge, trucks[idx]) <= L:
        bridge.append(trucks[idx])
        idx += 1

    elif idx == N:
        continue

    else:
        bridge.append(0)

print(time)