N = int(input())
arr = []
for i in range(N):
    book = input()
    arr.append(book)

s_arr = set(arr)
book_cnt = []

for b in s_arr:
    cnt = arr.count(b)
    book_cnt.append((b, cnt))

book_cnt.sort(key=lambda x:(-x[1], x[0]))

ans = book_cnt[0]
print(ans[0])