# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    arr_w = []
    arr_h = []

    for size in sizes :
        if size[0] < size[1] :
            arr_w.append(size[0])
            arr_h.append(size[1])
        else :
            arr_w.append(size[1])
            arr_h.append(size[0])

    return max(arr_h)*max(arr_w)


sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
r = 4000

print(solution(sizes))