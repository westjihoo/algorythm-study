# https://school.programmers.co.kr/learn/courses/30/lessons/17678

def solution(n, t, m, timetable):
    answer = ""

    crewtime = []
    for tb in timetable :
        hour, min = tb.split(":")
        crewtime.append(int(hour)*60 + int(min))

    bustime = [9*60 + x*t for x in range(n)]

    idx = 0
    for bt in bustime :
        cnt = 0
        while cnt < m and idx < len(crewtime) and crewtime[idx] <= bt :
            idx += 1
            cnt += 1
        if cnt < m :
            answer = bt - 1
        elif cnt == m:
            answer = crewtime[idx - 1] - 1
        else :
            answer = crewtime[idx + 1] - 1

        # 맨 뒤에 줄을 설 경우,,,
        # cnt < m
        # cnt = m
        # cnt > m
        # 다음버스 출발 시간 -1분

    answer = str(format(answer//60, "02")) + ":" + str(format(answer%60, "02"))
    return answer


n = 2
t = 1
m = 2
timetable = ["09:00", "09:00", "09:00", "09:00"]
r = "08:59"

n = 2
t = 10
m = 2
timetable = ["09:10", "09:09", "08:00"]
r = "09:09"


# n = 10
# t = 60
# m = 45
# timetable = ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
# r = "18:00"

print(solution(n, t, m, timetable))