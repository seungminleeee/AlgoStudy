"""
[BOJ] 22233번: 가희와 키워드 / 실3

조건:
1. 시간 제한 1.5초
2. 최대 10개의 키워드에 대해 글을 작성
3. 메모장에 있는 키워드 수 구하는 문제

풀이:
1.
"""
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
keywords = set(input().strip() for _ in range(n))
for _ in range(m):
    blog = input().strip()
    used_keywords = set(blog.split(','))
    keywords -= used_keywords
    print(len(keywords))