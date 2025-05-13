T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    mx = 0
    ans = 0
    for i in range(N-1,-1,-1):
        if nums[i] >= mx:
            mx = nums[i]
        elif nums[i] < mx:
            ans += mx - nums[i]

    print(ans)
