# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    dic_count = {}
    pivot = 0
    cursor = 0
    result = 0

    for alphabet in s :
        if not alphabet in dic_count :
            dic_count[alphabet] = 1
        else : dic_count[alphabet] += 1

        for item in dic_count.items() :
            if s[pivot] != item[0] and dic_count[s[pivot]] == item[1] :
                result += 1

                if cursor + 1 <= len(s) :
                    pivot = cursor + 1
                    dic_count = {}

        cursor += 1

    if dic_count != {} : result += 1
    
    return result


s = "banana"
r = 3
s = "abracadabra"
r = 6
# s = "aaabbaccccabba"
r = 3
print(solution(s))