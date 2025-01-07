from collections import defaultdict

name = input()

# word 딕셔너리 만들기
word = defaultdict(int)
for n in name:
    word[n] += 1

# 딕셔너리 value가 홀수이면 cnt 증가
cnt = 0
for c in word.values():
    if c % 2 == 1:
        cnt += 1
    
    # 2 이상이면 종료
    if cnt >= 2:
        print("I'm Sorry Hansoo")
        exit()

ans = ""  # 팰린드롬 앞부분
we = [] # 팰린드롬 뒷부분
plus = "" # 홀수개 문자일 경우 사용

# 딕셔너리 key 값으로 정렬하고 팰린드롬 만들기
for w in sorted(word.keys()):
    while word[w] > 0:
        # 딕셔너리 value 값이 1일때 가운데 들어갈 문자
        if word[w] == 1 and plus == "":
            plus += w
            word[w] -= 1

        else:
            ans += w
            we.append(w)
            word[w] -= 2

# 팰린드롬 뒷부분 역순으로 정렬 후 문자열 만들기
we.sort(reverse=True)
wer = "".join(we)

answer = ans + plus + wer
print(answer)