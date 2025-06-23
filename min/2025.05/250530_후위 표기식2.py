N = int(input())
lst = list(input())

alpha_dict = {}
for i in range(N):
    num = int(input())
    alpha_dict[chr(ord('A') + i)] = num

calculator = ['+', '-', '/', '*']
stack = []

for l in lst:
    if l not in calculator:
        num = alpha_dict[l]
        stack.append(num)
    else:
        b = stack.pop()
        a = stack.pop()

        if l == '+':
            ret = a + b
        elif l == '-':
            ret = a - b
        elif l == '*':
            ret = a * b
        elif l == '/':
            ret = a / b

        stack.append(ret)

ans = format(stack[0], ".2f")
print(ans)