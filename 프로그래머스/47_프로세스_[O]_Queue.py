# https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    cnt = 1
    while priorities :
        target = max(priorities)
        poped = priorities.pop(0)
        
        if target != poped :
            priorities.append(poped)
        else : # target == poped
            if location == 0 :
                return cnt
            else :
                cnt += 1

        location -= 1
        if location < 0 :
            location = len(priorities)-1

    return 0

priorities = [2, 1, 3, 2]
location = 2
priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(solution(priorities, location))