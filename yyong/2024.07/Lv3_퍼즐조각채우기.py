from collections import deque

# 배열 회전 함수
def turn(arr):
    N = len(arr)
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[j][N-i-1] = arr[i][j]
    return new_arr

# 조각 확인 함수                         # 원래 visited를 파라미터로 안넣어줬는데 도대체 뭐가 틀리지????? 
def check_piece(a, b, table, visited):  # 이해할수 없어서 여기서 사용하는 인자를 다 파라미터로 넣어보니까 맞았음... 아직 함수 이해도가 부족한듯
    N = len(table)
    Q = deque([(a, b)])
    cur_piece = [(a, b)]
    visited[a][b] = 1

    while Q:
        cr, cc = Q.popleft()
        for k in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            nr, nc = cr + k[0], cc + k[1]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and table[nr][nc]:
                visited[nr][nc] = 1
                cur_piece.append((nr, nc))
                Q.append((nr, nc))

    return cur_piece


def solution(game_board, table):
    N = len(game_board)
    pieces = []
    visited = [[0] * N for _ in range(N)]
    answer = 0
    

    # 1. table에 주어진 각각의 조각 확인
    for a in range(N):
        for b in range(N):
            if table[a][b] and not visited[a][b]:
                pieces.append(check_piece(a, b, table, visited))
    
    # table의 조각 사용했는지 확인하는 리스트
    used = [0] * len(pieces)
    

    # 2. 맞춤 조각 확인
    for _ in range(4):
        game_board = turn(game_board)
        checked = [[0] * N for _ in range(N)]
        
        for i in range(N):
            for j in range(N):
                if not game_board[i][j] and not checked[i][j]:  # 2.1 게임보드에 빈칸이 있고, 검사하지 않은 부분이라면
                    cur_blank = [(i, j)]                        #     빈칸 체크 시작
                    Q = deque([(i, j)])
                    checked[i][j] = 1
                    
                    while Q:
                        cr, cc = Q.popleft()
                        for k in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                            nr, nc = cr + k[0], cc + k[1]
                            if 0 <= nr < N and 0 <= nc < N and not game_board[nr][nc] and not checked[nr][nc]:
                                checked[nr][nc] = 1
                                Q.append((nr, nc))
                                cur_blank.append((nr, nc))
                    
                    check_blank = list(map(lambda x: (x[0]-i, x[1]-j), cur_blank))  # 상대위치로 변경
                    
                    # 2.2 이 빈칸과 table에서 찾은 조각이 맞는 조각인지 확인
                    for p in range(len(pieces)):
                        piece = pieces[p]
                        new_piece = list(map(lambda x: (x[0]-piece[0][0], x[1]-piece[0][1]), piece))  # 상대위치로 변경
                        
                        if sorted(new_piece) == sorted(check_blank) and not used[p]:   # 2.3 상대위치 크기가 맞고, 사용하지 않은 조각이면
                            used[p] = 1
                            answer += len(piece)          # 정답에 빈칸 추가
                            for dr, dc in cur_blank:      # 빈칸 메꾸기  
                                game_board[dr][dc] = 1
                            break

    return answer
