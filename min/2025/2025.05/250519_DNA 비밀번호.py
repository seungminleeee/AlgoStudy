from collections import Counter

def check(cnt):
    global ans

    if cnt['A'] >= A and cnt['C'] >= C and cnt['G'] >= G and cnt['T'] >= T:
        ans += 1

S, P = map(int, input().split())
dna = list(input())
A, C, G, T = map(int, input().split())

ans = 0

password = dna[:P]
cnt = Counter(password)

check(cnt)

for i in range(1, S-P+1):
    left = dna[i-1]
    right = dna[i + P - 1]

    cnt[left] -= 1
    cnt[right] += 1

    check(cnt)

print(ans)