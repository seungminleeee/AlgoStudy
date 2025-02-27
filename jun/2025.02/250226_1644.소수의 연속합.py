"""
[BOJ] 1644번: 소수의 연속합 / 골드3
"""
n = int(input())  # (1 ≤ N ≤ 4,000,000)
prime_numbers = []
check = [False] * (n + 1)

# 소수 구하기
for i in range(2, n + 1):
    if not check[i]:
        prime_numbers.append(i)
    for j in range(i * 2, n + 1, i):
        check[j] = True

# 투 포인터
count = 0
left = 0
right = 0
cur_sum = 0 if not prime_numbers else 2

while left < len(prime_numbers):
    if cur_sum == n:
        count += 1
        cur_sum -= prime_numbers[left]
        left += 1
    elif cur_sum > n:
        cur_sum -= prime_numbers[left]
        left += 1
    else:
        right += 1
        if right < len(prime_numbers):
            cur_sum += prime_numbers[right]
        else:
            break

print(count)