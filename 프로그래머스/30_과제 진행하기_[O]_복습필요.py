# https://school.programmers.co.kr/learn/courses/30/lessons/176962

def solution(plans):
    
    for idx, p in enumerate(plans) :
        h, m = p[1].split(":")
        start = int(h)*60 + int(m)
        playtime = int(p[2])
        plans[idx][1] = start
        plans[idx][2] = playtime

    plans.sort(key = lambda x : x[1])

    stack = []
    finish = []
    left = 0

    for i in range(len(plans)) :
        name, start, playtime = plans[i]
        
        while stack :
            _name, _playtime = stack.pop()
            if left >= _playtime :
                left -= _playtime
                finish.append(_name)
            else :
                stack.append([_name, _playtime - left])
                break
        
        if i < len(plans)-1 :
            next_start = plans[i+1][1]
            left = next_start - start

        stack.append([name, playtime])
        
    while len(stack) != 0 :
        finish.append(stack.pop()[0])

    return finish


plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]
result = ["korean", "english", "math"]

plans = [["computer", "12:30", "100"], ["history", "14:00", "30"], ["music", "12:20", "40"] , ["science", "12:40", "50"]]
result = ["science", "history", "computer", "music"]

print(solution(plans))