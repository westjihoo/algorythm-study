# https://school.programmers.co.kr/learn/courses/30/lessons/42577

# 슬라이싱

# 문자열 SORT의 경우 전체 크기와 무관하게
# 앞자리의 수가 작으면 작다고 판단

# phone_book[i]의 문자열 길이만큼 그 다음 문자를 슬라이싱
# ['12', '123'] 에서 12의 길이만큼 123을 슬라이싱, 즉 12
# if '12' in '12' : 가 되어 False를 반환

def solution(phone_book):
    if len(phone_book) == 1 :
        return True
    
    phone_book.sort()

    for i in range(len(phone_book)-1) :
        if phone_book[i] in phone_book[i+1][:len(phone_book[i])]:
            return False
    return True

phone_book = ["12","123","1235","567","88"]
phone_book = ["123","456","789"]
print(solution(phone_book))