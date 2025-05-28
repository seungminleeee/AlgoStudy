N, M, B = map(int, input().split())

land = [list(map(int, input().split())) for _ in range(N)]

mn_time = float('inf')
mx_height = 0

for h in range(257):
  time = 0
  inven = B

  for i in range(N):
    for j in range(M):
      height = land[i][j]

      if height > h:
        inven += height - h
        time += 2 * (height - h)
      elif height < h:
        inven -= h - height
        time += (h - height)

  if inven >= 0:
    if time < mn_time or (time == mn_time and h >= mx_height):
      mn_time = time
      mx_height = h

print(mn_time, mx_height)