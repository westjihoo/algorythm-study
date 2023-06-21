# https://school.programmers.co.kr/learn/courses/30/lessons/70129


def solution(s):
    
    def recur(s) :
        if s == "1" :
            return [0, 0]
        else :
            return [
                    1 + recur(str(format(len(s) - s.count("0"), 'b')))[0],
                    s.count("0") + recur(str(format(len(s) - s.count("0"), 'b')))[1]
                    ]
        
    answer = recur(s)

    return answer

# rmv_0 = 0
s = "110010101001"
# rmv_0 += s.count("0")
# s.replace("0","")
# s = format(len(s) - rmv_0, 'b')

# print(s)
print(solution(s))