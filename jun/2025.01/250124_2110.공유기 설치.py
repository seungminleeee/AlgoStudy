"""
[BOJ] 2110번: 공유기 설치 / 골4

조건:
1. 시간 제한 2초
2. 집 개수 n, 공유기 개수 c
3. 공유기 간의 거리 최소화의 경우 중에서 가장 큰 거리 구하기

풀이:
1. 최적의 거리를 찾아야하기에 이분탐색 사용
2. 중간거리 mid로 공유기 설치할 수 있는지 탐색하면서 진행

시간복잡도 정렬(O(N log N)) + 이분탐색(O(log 최대 거리) * for문(O(n)) 예상
"""
n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

low = 1
high = house[-1] - house[0]
ans = 0

while low <= high:
    mid = (low + high) // 2

    # 첫 집에 와이파이 설치
    wifi = 1
    # 마지막 설치 집 기록용
    last_wifi = house[0]

    # 집 돌면서 공유기 설치
    for i in range(1, n):
        if house[i] - last_wifi >= mid:
            wifi += 1
            last_wifi = house[i]

    if wifi >= c:
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)