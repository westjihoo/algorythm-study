# https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    answer = True
    cnt_p = cnt_y = 0
    for i in s :
        if i == 'p' or i == 'P' : cnt_p += 1
        if i == 'y' or i == 'Y' : cnt_y += 1
    if cnt_p != cnt_y : answer = False
    return answer

print(solution("pPoooyY"))