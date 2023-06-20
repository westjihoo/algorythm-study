# https://school.programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    answer = -1
    arr_n = []
    i = 1

    while i*i <= n :
        arr_n.append(i*i)
        i += 1
    print(arr_n)
    if n in arr_n :
        x = arr_n.index(n)
        answer = (x+2)**2

    return answer


print(solution(121))