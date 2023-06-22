# https://school.programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    answer = ["ICN"]
    tickets.sort(key = lambda x : x[1])

    depart = "ICN"
    while len(tickets) > 0 :
        for idx, t in enumerate(tickets) :
            if depart == t[0] :
                answer.append(t[1])
                depart = t[1]
                tickets.remove(t)

    return answer



tickets	= [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
r = ["ICN", "JFK", "HND", "IAD"]

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
r = ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

print(solution(tickets))