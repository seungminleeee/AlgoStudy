N = int(input())
city = list(map(int, input().split()))
gas = list(map(int, input().split()))

pre_gas = float('inf')
total_gas = 0
for i in range(N-1):
    if gas[i] < pre_gas:
        pre_gas = gas[i]
    total_gas += pre_gas*city[i]

print(total_gas)