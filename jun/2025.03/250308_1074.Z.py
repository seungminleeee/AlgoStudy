"""
[BOJ] 1074번: Z / 골드5
"""
def z(n, row, col):
    check = 2 ** (n - 1)

    if n == 0:
        return 0

    # 제 1사분면
    if row < check and col < check:
        return z(n - 1, row, col)

    # 제 2사분면
    elif row < check and col >= check:
        return check ** 2 + z(n - 1, row, col - check)

    # 제 3사분면
    elif row >= check and col < check:
        return (2 * (check ** 2)) + z(n - 1, row - check, col)

    # 제 4사분면
    elif row >= check and col >= check:
        return (3 * (check ** 2)) + z(n - 1, row - check, col - check)

n, r, c = map(int, input().split())  # 1 ≤ N ≤ 15 / 0 ≤ r, c < 2N

print(z(n, r, c))