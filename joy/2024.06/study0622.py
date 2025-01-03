# 백준 실4 1205번 등수 구하기 
# 메모리 31120 시간 40 
N, score, P = map(int, input().split()) # N 리스트에 있는 점수 score 태수 점수 P 리스트에 올라갈 수 있는 점수 개수
if N > 0: # N이 0보다 클 때 
    arr = list(map(int, input().split())) # arr 인풋 
else: # 없으면 빈 배열 만들어주기 
    arr = []

if len(arr) == 0: # 빈 배열이면 그냥 들어간 점수가 1등임 
    print(1)
else:
    arr.append(score) # arr 에 score점수 넣어주고
    arr.sort(reverse=True) # 정렬함 
    win = arr.index(score) + 1 # 그랬을 때 순위는 index의 번호에 1 더해준 값! (같은 점수면 다 똑같은 등수니까..)
    if win > P or (len(arr) > P and arr[P-1] == score and arr[P-1] == arr[P]): 
        # 만약에 등수가 P보다 크거나 / 흠.... arr[P] == score 해도 맞네.. 암튼 끝값이랑 같으면 이건 등수에 포함할 수 없음 
        print(-1) # -1 출력
    else:
        print(win) # 나머지는 등수 출력

    
# elif score <= arr[-1]:
#     if len(arr) == P:
#         print(-1)
#     elif len(arr) < P:
#         arr.insert(0, score)
#         arr.sort()
#         arr_idx = list(filter(lambda x:arr[x] == score, range(len(arr))))
#         print(arr_idx[-1] + 1)
# else:
#     arr.insert(0, score)
#     arr.sort()
#     arr_idx = list(filter(lambda x: arr[x] == score, range(len(arr))))
#     print(arr_idx[-1] + 1)


