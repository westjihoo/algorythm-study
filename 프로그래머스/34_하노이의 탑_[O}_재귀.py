# https://school.programmers.co.kr/learn/courses/30/lessons/12946

def solution(n):
    answer = []

    def recur(n, first, second, third):
        
        if n == 1 :
            answer.append([first,third])
            return

        else :
            recur(n-1, first, third, second)
            answer.append([first,third])
            recur(n-1, second, first, third)

    recur(n, 1, 2, 3)

    return answer



print(solution(2))