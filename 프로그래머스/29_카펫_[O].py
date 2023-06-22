# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    
    total = brown + yellow
    arr_combi = []
    answer = []

    for x in range(1,total+1) :
        if total%x==0 :
            if x >= total//x and total//x > 2:
                arr_combi.append([x, total//x])

    for case in arr_combi :
        rect_round = (case[0]+case[1]) * 2 - 4
        if brown == rect_round and yellow == (total - rect_round) :
            answer.append(case[0])
            answer.append(case[1])
            
    return answer



brown = 10
yellow = 2
r = [4, 3]

print(solution(brown, yellow))