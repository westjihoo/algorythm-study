# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ""
    first_met = True

    for alphabet in s :
        if alphabet == " " :
            first_met = True

        if first_met == True :
            if 97 <= ord(alphabet) and ord(alphabet) <= 122 :
                answer += chr(ord(alphabet) - 32)
                first_met = False
            elif alphabet == " " :
                answer += alphabet
            else :
                answer += alphabet
                first_met = False
        else :
            if 65 <= ord(alphabet) and ord(alphabet) <= 90 :
                answer += chr(ord(alphabet) + 32)
            else :
                answer += alphabet

    return answer

s = "3people unFollowed me"
r = "3people Unfollowed Me"
s = "for the last week"
r = "For The Last Week"

print(solution(s))