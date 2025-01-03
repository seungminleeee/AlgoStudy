N = int(input())
pattern = input()
code = pattern.split('*')
code1 = code[0]
code2 = code[1]
for i in range(N):
    string = input()
    if len(string) < len(code1) + len(code2):
        print('NE')
    elif string[0:len(code1)] == code1 and string[-len(code2):] == code2:
        print('DA')
    else:
        print('NE')
