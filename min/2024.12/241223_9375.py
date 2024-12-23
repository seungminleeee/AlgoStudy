from collections import defaultdict

T=int(input())

for t in range(1, T+1):
    N = int(input())
    clothes = defaultdict(int)

    for n in range(N):
        name, type = input().split()
        clothes[type] += 1

    ans = 1
    for c in clothes.values():
        ans *= c+1

    print(ans-1)

# 처음엔 set으로 input 받은 걸 다 리스트에 넣은 다음 돌면서 count 세려고 했는데
# 시간초과 날거 같아서 찾아보니 딕셔너리 쓰면 되는게 생각나서 하다가 계속 오류나서
# 지피티 돌렸더니 defalutdict 쓰라고 함!