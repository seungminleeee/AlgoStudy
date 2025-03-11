# 솔트 말고 어캐하죠 ...? 메모리랑 시간 오바네 .. 
# 중간에 영어랑 수학 점수 바꿔서 해가지고 자꾸 틀림 ㅜ
N = int(input())
result = []
for i in range(N):
    name, kor, eng, math = map(str, input().split())
    kor, eng, math = int(kor), int(eng), int(math)
    result.append((name, kor, eng, math))

result.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in range(N):
    print(result[i][0])