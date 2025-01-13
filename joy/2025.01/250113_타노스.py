# 1은 앞에서부터 0은 뒤에서 부터 빼주면 된다..
string = list(input())
zero_cnt = string.count('0') // 2
one_cnt = string.count('1') // 2

for i in range(one_cnt):
    string.pop(string.index('1'))

for j in range(zero_cnt):
    string.pop(-string[::-1].index('0')-1)

print(''.join(string))




# string = input()
# dict = {}
# for i in string:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1

# zero = 0
# one = 0

# for i in dict:
#     if i == '1':
#         one = dict['1'] // 2
#     elif i == '0':
#         zero = dict['0'] //2

# print('0'*zero+'1'*one)


