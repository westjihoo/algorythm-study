# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []

    for cmd in commands :
        tmp = array[cmd[0]-1:cmd[1]]
        tmp = sorted(tmp)
        answer.append(tmp[cmd[2]-1])
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
r=[5, 6, 3]

print(solution(array, commands))