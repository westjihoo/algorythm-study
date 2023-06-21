# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True
    arr_brk = []

    for i in range(len(s)) :
        bracket = s[i]

        if i == 0 and bracket == ")" :
            answer = False
            break

        if bracket == "(" :
            arr_brk.append(bracket)
        elif len(arr_brk) > 0 : 
            arr_brk.pop()
        else :
            answer = False
            break

    if len(arr_brk) != 0 :
        answer = False

    return answer


s = "(())()" # T
s = ")()(" # F
s = "(()(" # F

print(solution(s))