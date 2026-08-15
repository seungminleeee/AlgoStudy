from collections import defaultdict

def solution(board):   
    D = defaultdict(int)
    
    for i in range(3):
        for j in range(3):
            D[board[i][j]] += 1
    
    if D['O'] < D['X'] or D['O'] > D['X'] + 1:
        return 0
    
    def win(a):
        # 가로
        for i in range(3):
            if board[i][0] == a and board[i][0] == board[i][1] == board[i][2]:
                return True
        # 세로
        for j in range(3):
            if board[0][j] == a and (board[0][j] == board[1][j] == board[2][j]):
                return True
        # 대각선
        if board[0][0] == a and (board[0][0] == board[1][1] == board[2][2]):
            return True
        # 대각선
        if board[2][0] == a and (board[2][0] == board[1][1] == board[0][2]):
            return True
        
        return False
    
    O = win("O")
    X = win("X")
    
    if O and X:
        return 0
    
    if O and D["O"] != D["X"] + 1:
        return 0
    
    if X and D["O"] != D["X"]:
        return 0
    
    return 1