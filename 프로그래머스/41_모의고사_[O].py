# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    people = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    total = {1 : 0, 2 : 0, 3 : 0}
    
    for idx, a in enumerate(answers) :
        for x in range(3) :
            if a == people[x][idx%len(people[x])] :
                total[x+1] += 1
            
    max_s = 0
    for t in total.values() :
        if t > max_s : max_s = t

    answer = [ k for k,v in total.items() if max_s == v ]
    return answer

answers = [1,2,3,4,5]
solution(answers)