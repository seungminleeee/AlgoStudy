N = int(input())
pat = list(input().split("*"))
start = pat[0]
end = pat[1]

for i in range(N):
    file = input()

    if len(file) < len(start) + len(end):
        print("NE")
        continue
    # 1. 처음에 길이 조건 확인 안해서 틀리고
    # 2. 그다음은 continue 처리 안해줘서 틀림

    f_start = file[:len(start)]
    f_end = file[-len(end):]
    # 슬라이싱 넘 오랜만에 해서 찾아보고 함 ;;

    if f_start == start and f_end == end:
        print("DA")
    else:
        print("NE")