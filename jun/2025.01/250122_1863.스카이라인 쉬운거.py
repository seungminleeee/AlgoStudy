"""
[BOJ] 1863번: 스카이라인 쉬운거 / 골4

조건:
1. 시간 제한 2초
2. 건물 몇 개인가?

생각:
1. x좌표 필요 없어 보임
2. y가 가다가 낮아지면 건물 끝 (카운트)
3. 남은 건물 세는 것도 해줘야 함.
4. 높이 문제는 보통 스택으로 푸니까 도전
"""
n = int(input())

stack = []
ans = 0

for _ in range(n):
    x, y = map(int, input().split())

    # 건물 카운트
    while stack and stack[-1] > y:
        stack.pop()
        ans += 1

    # 건물 추가
    if not stack or stack[-1] < y:
        stack.append(y)

# 남은 건물 카운트 (0은 제외)
ans += len(stack) - stack.count(0)
print(ans)