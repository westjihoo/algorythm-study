# https://school.programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    tmp = ""
    i = 0
    l = len(strings)

    while l > i :
            
        for j in range(l-1-i) :
            if strings[j][n] > strings[j+1][n] :
                tmp = strings[j]
                strings[j] = strings[j+1]
                strings[j+1] = tmp
            elif strings[j][n] == strings[j+1][n] :
                if strings[j] > strings[j+1] :
                    tmp = strings[j]
                    strings[j] = strings[j+1]
                    strings[j+1] = tmp
        i += 1

    return strings

strings = ["abce", "abcd", "cdx"]
n = 2
r = ["abcd", "abce", "cdx"]

print(solution(strings, n))