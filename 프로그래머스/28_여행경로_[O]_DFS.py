# https://school.programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    route = dict()
    
    for (start, end) in tickets :
        # route에 key, value를 추가하는데
        # route에 start라는 key가 있으면 value를 가져와
        #  +[end]를 행하고,
        # start라는 key가 없으면 []를 대입하여
        #  [] + [end] 가 됨
        route[start] = route.get(start, []) + [end]
    
    for r in route.keys() :
        route[r].sort(reverse=True)

    stack = ['ICN']
    path = []
    
    while stack :
        top = stack[-1]

        # route에 top이 key로 없거나
        # route[top]의 길이가 0이면 ( value가 없으면 )
        if top not in route or len(route[top]) == 0 :
            # stack의 마지막 값을 path로 이동
            path.append(stack.pop())
        
        # route에 top이 key로 있고
        # route[top]의 길이가 1 이상이면
        # ( value(도착지) 가 남아있으면 )
        else :
            # route[top] 마지막 값(도착지)를 stack으로 이동
            stack.append(route[top][-1])
            route[top] = route[top][:-1]

            # 위에서 top을 stack.pop()로 받는다면 아래도 가능
            # stack.append(top)
            # stack.append(route[top].pop())
    
    return path[::-1]



tickets	= [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
r = ["ICN", "JFK", "HND", "IAD"]

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
r = ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

print(solution(tickets))