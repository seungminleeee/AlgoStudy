N = int(input())
arr = [input() for _ in range(N)]

def num_sum(code):
    total = 0 
    for i in code:
        if i.isdigit():
            total += int(i)
    return total 

arr.sort(key = lambda x: (len(x), num_sum(x), x))

for i in arr:
    print(i)