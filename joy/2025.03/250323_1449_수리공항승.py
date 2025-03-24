N, L = map(int, input().split())
pipe = sorted(list(map(int, input().split())))
tape = 0
tape_last = 0

for i in pipe:
    if i > tape_last:
        tape += 1
        tape_last = i + L - 0.5
print(tape)