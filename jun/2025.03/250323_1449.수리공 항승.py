"""
[BOJ] 1449번: 수리공 항승 / 실버3
"""
n, l = map(int, input().split())  # N과 L은 1,000보다 작거나 같은 자연수
locations = list(map(int, input().split()))
locations.sort()

answer = 0
end = 0
for location in locations:
    if location > end:
        answer += 1
        end = (location - 0.5) + l

print(answer)