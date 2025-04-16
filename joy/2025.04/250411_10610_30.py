N = input()
lst = list(map(int, N))
if '0' not in N:
    print(-1)
elif sum(lst) % 3 != 0: # 각 자리수의 합이 3의 배수가 아니면 30의 배수가 될 수 없음
    print(-1)
else:
    print(''.join(sorted(N, reverse=True)))

# from itertools import permutations

# N = input()
# n = list(N)

# comb = set(list(permutations(n, len(n))))

# valid = []
# for num in comb:
#     if num[-1] != '0':
#         continue
#     result = int(''.join(num))
#     if result % 30 == 0:
#         valid.append(result)

# if valid:
#     print(max(valid))
# else:
#     print(-1)