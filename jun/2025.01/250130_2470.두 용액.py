"""
[BOJ] 2470번: 두 용액 / 골5

조건:
1. 두 용액의 특성값의 합이 0에 가장 가까운 것을 구하기
2. 2 <= n <= 100,000
3. 수들은 -1,000,000,000 이상 1,000,000,000 이하
4. 두 개 이상일 경우에는 그 중 아무것이나 하나를 출력
"""
n = int(input())
solution = list(map(int, input().split()))
solution.sort()
left = 0
right = n - 1
target_sum = float('inf')
result = None
while left < right:
    cur_sum = solution[left] + solution[right]
    if abs(cur_sum) < abs(target_sum):
        target_sum = cur_sum
        result = (solution[left], solution[right])
    if cur_sum == 0:
        result = (solution[left], solution[right])
        break
    if cur_sum < 0:
        left += 1
    else:
        right -= 1
print(result[0], result[1])