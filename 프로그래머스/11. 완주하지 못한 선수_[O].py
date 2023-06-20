# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    dic_comp = {}

    for person in completion :
        if not person in dic_comp :
            dic_comp[person] = 1
        elif dic_comp[person] >= 1 :
            dic_comp[person] += 1

    while len(participant) > 0 :
        poped = participant.pop()
        
        if poped in dic_comp and dic_comp[poped] >= 1 :
            dic_comp[poped] -= 1
        else :
            return poped
    return 0

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
re = "mislav"

print(solution(participant, completion))