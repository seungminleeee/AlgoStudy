N = int(input())
nums = list(map(int, input().split()))

set_nums = sorted(set(nums))

dict_nums = {}
for i in range(len(set_nums)):
    key = set_nums[i]
    dict_nums[key] = i

lst = [0]*N
for j in range(N):
    lst[j] = dict_nums[nums[j]]

print(*lst)