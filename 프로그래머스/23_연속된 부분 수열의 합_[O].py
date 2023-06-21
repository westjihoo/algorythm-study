# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    answer = []
    sum = 0
    r = -1
    l = 0
    
    while True :
        
        if sum < k :
            r += 1
            if r >= len(sequence) :
                break
            sum += sequence[r]

        else :
            sum -= sequence[l]
            if l >= len(sequence) :
                break
            l += 1
        
        if sum == k :
            answer.append([l,r])

    answer.sort(key=lambda x : (x[1]-x[0], x[0]))
    
    return answer[0]

sequence = [1, 2, 3, 4, 5]
k = 7

print(solution(sequence, k))