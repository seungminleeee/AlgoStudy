def sequence(n):
    
    if not memo[n]:
        memo[n] = sequence(n-2) + sequence(n-3)
    
    return memo[n]

memo = [0] * 101
memo[1] = memo[2] = memo[3] = 1

for _ in range(int(input())):
    num = int(input())

    print(sequence(num))