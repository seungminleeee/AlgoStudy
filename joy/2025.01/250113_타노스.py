# 1은 앞에서부터 0은 뒤에서 부터 빼주면 된다..
# 카운트도 딕셔너리 말고 count 로 쉽게 바꿨음
string = list(input())
zero_cnt = string.count('0') // 2
one_cnt = string.count('1') // 2

for i in range(one_cnt):
    string.pop(string.index('1'))

for j in range(zero_cnt):
    string.pop(-string[::-1].index('0')-1)

print(''.join(string))


# 실패작 ;;; 
# 처음엔 그냥 갯수만큼 하고 작은 수 만드는 줄 알고 .. 이러니까 25점 맞음 ㅋㅋ;;
string = input()
dict = {}
for i in string:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

zero = 0
one = 0

for i in dict:
    if i == '1':
        one = dict['1'] // 2
    elif i == '0':
        zero = dict['0'] //2

print('0'*zero+'1'*one)


