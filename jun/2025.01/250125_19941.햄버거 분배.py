"""
[BOJ] 19941번: 햄버거 분배 / 실3

조건:
1. 시간 제한 0.5초
2. 식탁의 길이 n, 햄버거를 선택할 수 있는 거리 k
3. 햄버거를 먹을 수 있는 사람의 최대  구하기
4. 1 <= n <= 20,000 / 1 <= k <= 10

풀이:
1. 리스트 for문으로 enumerate로 인덱스 이용
2. P가 나오면 양 옆 k거리만큼 체크 후 H가 있으면 H 인덱스 저장(중복 제거)
3. 개수 출력
"""
n, k = map(int, input().split())
arr = list(input().strip())

cnt = 0
check = [False] * n

for idx, i in enumerate(arr):
    if i == 'P':
        for j in range(max(0, idx-k), min(n, idx+k+1)):
            if arr[j] == 'H' and not check[j]:
                cnt += 1
                check[j] = True
                break

print(cnt)