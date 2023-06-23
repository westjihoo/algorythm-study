# https://school.programmers.co.kr/learn/courses/30/lessons/62048

def solution(w,h):
    total = w*h
    gcd_x = gcd(w, h)
        
    return total-(w+h-gcd_x)

def gcd(x, y) :
    while y > 0 :
        x, y = y, x%y
    return x


w = 8
h = 12
print(solution(w,h))