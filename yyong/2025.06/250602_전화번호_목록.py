def solution(phone_book):
    answer = True

    phone_book.sort()  # 문자열 정렬
    
    for p in range(len(phone_book)-1):
        if phone_book[p] == phone_book[p+1][:len(phone_book[p])]:
            answer = False
    return answer
