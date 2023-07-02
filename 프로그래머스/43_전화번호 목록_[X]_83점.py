# https://school.programmers.co.kr/learn/courses/30/lessons/42577

# 완전탐색
# 테스트 13, 14번 실패 (오답)
# 효율성 3, 4번 실패 (시간초과)

def solution(phone_book):
    
    phone_book.sort()
    i = 1
    for phone in phone_book :
        for idx in range(i, len(phone_book)):
            if phone_book[idx].find(phone) != -1 :
                return False
        i += 1

    return True

phone_book = ["12","123","1235","567","88"]
phone_book = ["123","456","789"]
print(solution(phone_book))