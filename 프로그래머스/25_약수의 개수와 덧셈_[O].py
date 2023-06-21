# https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    answer = 0
    
    for i in range(left,right+1) :

        cnt = 0
        
        for x in range(1,i+1) :
            if i%x==0 :
                cnt += 1

        if cnt % 2 == 0 :
            answer += i
        else :
            answer -= i

    return answer

left = 13
right = 17
result = 43

# left = 24
# right = 27
# result = 52

print(solution(left, right))