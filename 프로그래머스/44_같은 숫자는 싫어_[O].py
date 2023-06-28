# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    for a in arr :
        if len(answer) < 1 :
            answer.append(a)
        poped = answer.pop()
        if poped == a :
            answer.append(a)
        else :
            answer.append(poped)
            answer.append(a)
    
    return answer


arr = [1,1,3,3,0,1,1]
r = [1,3,0,1]
print(solution(arr))