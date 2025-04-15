def func(lst):
    lst.sort(reverse=True)

    if lst[-1] != 0:
        return -1

    if sum(lst) % 3 != 0:
        return -1

    ans = "".join(map(str,lst))
    return ans

nums = list(map(int, input()))
print(func(nums))