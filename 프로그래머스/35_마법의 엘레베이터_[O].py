# https://school.programmers.co.kr/learn/courses/30/lessons/148653

def solution(storey):
    answer = 0

    while storey != 0 :
        n = storey % 10
        storey = storey // 10
        
        if n >= 6 :
            answer += 10 - n
            storey += 1
        elif n == 5 and storey%10 >= 5 :
            answer += 10 - n
            storey += 1
        else :
            answer += n
    
    return answer

storey = 2554
print(solution(storey))