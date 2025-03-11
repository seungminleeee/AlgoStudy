from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_possible(grid, y, x, n, m):
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n + 2 and 0 <= nx < m + 2:
            if grid[ny][nx] == '#':
                return True
    return False

def truck(grid, target, n, m):
    queue = deque()
    for i in range(n + 2):
        for j in range(m + 2):
            if grid[i][j] == target and is_possible(grid, i, j, n, m):
                queue.append((i, j))

    while queue:
        y, x = queue.popleft()
        if grid[y][x] != target:
            continue
        grid[y][x] = '#'

        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n + 2 and 0 <= nx < m + 2 and grid[ny][nx] == target:
                if is_possible(grid, ny, nx, n, m):
                    queue.append((ny, nx))

def crane(grid, target, n, m):
    for i in range(n + 2):
        for j in range(m + 2):
            if grid[i][j] == target:
                grid[i][j] = '#'

def solution(storage, requests):
    # '#'으로 둘러 싸기
    n = len(storage)
    m = len(storage[0])
    grid = []
    # '#' 넣기
    grid.append(['#'] * (m + 2))
    for row in storage:
        grid.append(['#'] + list(row) + ['#'])
    grid.append(['#'] * (m + 2))

    for request in requests:
        target = request[0]
        # 지게차
        if len(request) == 1:
            truck(grid, target, n, m)
        # 크레인
        elif len(request) == 2:
            crane(grid, target, n, m)

    answer = 0
    # '#' 아닌거 카운트
    for i in range(n + 2):
        for j in range(m + 2):
            if grid[i][j] != '#':
                answer += 1

    return answer


print(solution(["AZWQY", "CAABX", "BBDDA", "ACACA"], ["A", "BB", "A"]))