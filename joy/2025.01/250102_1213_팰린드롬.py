# 짝수 길이 글자는 글자가 홀수 갯수인게 있으면 안되고 
# 홀수 길이 글자는 글자가 홀수 갯수인게 1개만 있어야 함

N = list(input())
word = {} #AAABB 라 하자 'A':3, 'B':2 
for i in N:
    if i in word:
        word[i] += 1
    else:
        word[i] = 1

odd_cnt = 0
odd_char = ""
palin = ""

for char, cnt in sorted(word.items()): 
    if cnt % 2 != 0: #value 값이 홀수면
        odd_cnt += 1 # cnt 를 높여준다 
        odd_char = char # 그리고 odd_char 안에 char = A 를 넣어둔다 
    palin += char * (cnt // 2) # A * 1 = A (반만 넣어줌)

if odd_cnt > 1: # 홀수 카운트가 1보다 크면 쏘리 출력
    print("I'm Sorry Hansoo")
else:
    result = palin + odd_char + palin[::-1] 
    # 아니면 반만 넣은 팰린드롬 + 홀수 문자 + 반넣은거 반대로 한거 출력 
    print(result)