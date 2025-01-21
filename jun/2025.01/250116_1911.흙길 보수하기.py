"""
[BOJ] 1911번: 흙길 보수하기 / 골5

조건:
1. 시간 제한 2초

생각:
1. 처음 시도는 리스트에 최대값으로 False로 load 만들고 웅덩이 True로 채워서 카운팅했는데 메모리 초과
2. 마지막 지점 저장해서 while문으로 카운팅했는데 시간 초과
3. 마지막 지점 저장하면서 if 문으로 계산식을 통해 해결 (최종 시간 복잡도 정렬 때문에 O(N*log^N) 예상)
"""
N, L = map(int, input().split())

load = []
for _ in range(N):
    s, e = map(int, input().split())
    load.append((s, e))

load.sort(key=lambda x: x[0])

ans = 0
last = 0
for s, e in load:
    if last < s:
        last = s

    if last < e:
        length = e - last
        board = (length + L - 1) // L
        ans += board
        last += board * L

print(ans)