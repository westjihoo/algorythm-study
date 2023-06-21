# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    
    dic = {}
    
    for clothe, type in clothes:
        dic[type] = dic.get(type, 0) + 1
    
    answer = 1
    for value in dic.items() :
        answer *= value[1] + 1
        
    answer -= 1
    return answer