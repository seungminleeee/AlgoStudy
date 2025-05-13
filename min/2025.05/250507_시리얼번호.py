N = int(input())
nums = [input() for _ in range(N)]
nums.sort(key=lambda x:(len(x), sum(int(ch) for ch in x if ch.isdigit()), x))

for num in nums:
    print(num)