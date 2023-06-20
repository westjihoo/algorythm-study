# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    result = cursor = sum = 0
    dic_count = {}

    while len(s) > 0 :
        if cursor == len(s) : break

        if not s[cursor] in dic_count : dic_count[s[cursor]] = 1
        else : dic_count[s[cursor]] += 1

        for item in dic_count.items() :
            if s[0] != item[0] : sum += item[1]

        if dic_count[s[0]] == sum :
            result += 1
            s = s[cursor+1:]
            cursor = -1
            dic_count = {}

        sum = 0
        cursor += 1

    if dic_count != {} : result += 1

    return result


s = "banana"
r = 3
s = "aaccccbb"
r = 6
s = "aaabbaccccabba"
r = "3"
print(solution(s))