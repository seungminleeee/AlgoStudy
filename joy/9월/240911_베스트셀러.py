# 딕셔너리 정리까지는 했는데 정렬하는 법을 까묵어서 검색해봣엉 .. 
# 딕셔너리는 sort 가 외않되! sorted 해야댐
# 그리고 - 붙으면 내림차순 + 면 오름차순이라고 하네요 .. 
# 숫자로는 큰거부터 같으면 이름순으로 오름차순이니까 !  

n = int(input())
book = {}
for i in range(n):
  string = input()
  if string not in book:
    book[string] = 1
  else:
    book[string] += 1

lst = sorted(book.items(), key = lambda x: (-x[1], x[0]))

print(lst[0][0])