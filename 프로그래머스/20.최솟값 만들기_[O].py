# https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    answer = 0

    A.sort(reverse = True)
    B.sort(reverse = False)
    print(A, B)

    for i in range(len(A)) :
        answer += A.pop() * B.pop()

    return answer

A = [1, 4, 2]
B = [5, 4, 4]

print(solution(A,B))