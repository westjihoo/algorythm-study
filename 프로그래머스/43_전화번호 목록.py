# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    
    phone_book.sort()
    for i in range(1, len(phone_book), 2) : 
        tmp = ""
        for c in phone_book[i] :
            tmp += c
            if phone_book[i-1].find(tmp) != -1 :
                return False
            if phone_book[i+1].find(tmp) != -1 :
                return False
            
    return True

phone_book = ["12","123","1235","567","88"]
phone_book = ["123","456","789"]
solution(phone_book)