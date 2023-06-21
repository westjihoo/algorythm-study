# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    arr_int = list(map(int, s.split()))
    mi = str(min(arr_int))
    ma = str(max(arr_int))
    return mi+" "+ma


s = "1 2 3 4"
s = "-1 -2 -3 -4"
print(solution(s))