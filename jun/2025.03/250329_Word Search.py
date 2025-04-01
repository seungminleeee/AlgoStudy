"""
[NCD] Word Search / Mid
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        visited = [[False] * m for _ in range(n)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(y, x, idx):
            if idx == len(word):
                return True
            if not (0 <= y < n and 0 <= x < m):
                return False
            if visited[y][x] or board[y][x] != word[idx]:
                return False

            visited[y][x] = True
            for dy, dx in directions:
                if dfs(y + dy, x + dx, idx + 1):
                    return True
            visited[y][x] = False
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False