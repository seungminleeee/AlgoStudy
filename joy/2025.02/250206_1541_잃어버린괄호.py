string = input()
number = []
ope = []
num = ""

for char in string:
    if char.isdigit():
        num += char 
    else:
        number.append(int(num))
        ope.append(char)
        num = ""

number.append(int(num))

# - 가 나오면 다 괄호로 묶어줘서 빼면 됨 .. 
result = number[0]
minus = False

for i in range(len(ope)):
    if ope[i] == '-':
        minus = True
    if minus:
        result -= number[i + 1]
    else:
        result += number[i + 1]

print(result)
