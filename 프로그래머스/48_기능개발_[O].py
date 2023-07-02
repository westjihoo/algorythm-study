# https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    remain = []
    for i in range(len(speeds)) :
        if (100 - progresses[i]) % speeds[i] == 0 :
            remain.append((100 - progresses[i]) // speeds[i])
        else :
            remain.append(((100 - progresses[i]) // speeds[i])+1)

# [5, 10, 1, 1, 20, 1]
# [7, 3, 9]
    tmp, cnt = remain[0], 1
    for i in range(1,len(remain)) :
        if tmp >= remain[i] :
            cnt += 1
        else :
            answer.append(cnt)
            tmp, cnt = remain[i], 1
    answer.append(cnt)

    return answer


progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
result = [1, 3, 2]

# progresses = [93, 30, 55]
# speeds = [1, 30, 5]

print(solution(progresses, speeds))