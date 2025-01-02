a1, b1 = input().split()
a2, b2 = input().split()

a1 = int(a1)
a2 = int(a2)
b1 = int(b1)
b2 = int(b2)

sum_b = b1*b2
sum_a = a1*b2 + a2*b1

for i in range(min(sum_a,sum_b), 1, -1):
    if sum_a % i == 0 and sum_b % i == 0:
        sum_b //= i
        sum_a //= i
        break

print(sum_a, sum_b)