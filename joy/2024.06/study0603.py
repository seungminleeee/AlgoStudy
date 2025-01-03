# 최대공약수와 최소공배수
num1, num2 = map(int, input().split())
small_num = min(num1, num2)
gcd_lst = [1, ]
for i in range(2, small_num + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd_lst.append(i)

gcd = gcd_lst.pop()
lcm = (num1 // gcd) * (num2 // gcd) * gcd

print(gcd)
print(lcm)