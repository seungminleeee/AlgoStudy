import sys
input=sys.stdin.readline

left = list(input().strip())
M = int(input())
right = []

for _ in range(M):
    command = input().split()

    if command[0] == 'L':
        if not left:
            continue
        s = left.pop()
        right.append(s)
    elif command[0] == 'D':
        if not right:
            continue
        s = right.pop()
        left.append(s)
    elif command[0] == 'B':
        if not left:
            continue
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

ans = left + right[::-1]
print(''.join(ans))