"""
[BOJ] 1541번: 잃어버린 괄호 / 실버2

1. 세준이와 양수는 +,-,괄호를 가지고 식을 만들고 나서 모두 지웠음.
2. 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 함.
"""
def solve(modify):
    arr = []
    change = ""
    for i in range(len(modify)):
        if modify[i] == "+":
            arr.append(int(change))
            arr.append("+")
            change = ""
        elif modify[i] == "-":
            arr.append(int(change))
            arr.append("-")
            change = ""
        elif i == len(modify) - 1:
            change += modify[i]
            arr.append(int(change))
        else:
            change += modify[i]

    ans = arr[0]
    negative = False
    for i in range(1, len(arr), 2):
        operator = arr[i]
        num = arr[i + 1]

        if operator == "-": negative = True
        if negative: ans -= num
        else: ans += num

    return ans

modify = input().strip()
print(solve(modify))