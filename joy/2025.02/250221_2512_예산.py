N = int(input())
budget = list(map(int, input().split()))
limit = int(input())
max_bud = 0 # 상한값
left, right = 0, max(budget)

while left <= right:
    mid = (left + right) // 2

    sum_bud = 0
    for i in budget:
        sum_bud += min(mid, i)
    
    if sum_bud <= limit:
        max_bud = mid
        left = mid + 1
    else:
        right = mid - 1

print(max_bud)


# N = int(input())
# budget = list(map(int, input().split()))
# limit = int(input())
# sum_bud = sum(budget)

# if sum_bud <= limit:
#     print(max(budget))
# else:
#     max_bud = min(budget)

#     while True:
#         sum_bud = 0
#         for i in budget:
#             sum_bud += min(max_bud, i)
        
#         if sum_bud > limit:
#             max_bud -= 1 
#             break
#         else:
#             max_bud += 1
    
#     print(max_bud)
       
        
            