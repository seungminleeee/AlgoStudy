# 문자열의 순서 바꾸면 안됨 -> 주어진 순서에서 pop 하듯이 삭제 가능
# 순서대로 순회하면서
# 1이 나올때 : 갯수의 반절만큼 무시했으면 append 아니면 무시
# 0이 나올때 : 갯수 다 안찼으면 append 아니면 무시

from collections import defaultdict

S = input()
char = defaultdict(int)
result = ''

for s in S:
    char[s] += 1

append_0 = 0
pass_1 = 0

for s in S:

    # 현재 0일 때 : 반절만큼 입력 했으면 나머지는 무시
    if s == '0' and append_0 < char['0'] // 2:
        result += s
        append_0 += 1

    # 현재 1일 때 : 반절만큼 무시하고 그 이상일땐 append
    if s == '1' and pass_1 >= char['1'] // 2:
        result += s
    elif s == '1' and pass_1 < char['1'] // 2:
        pass_1 += 1

print(result)