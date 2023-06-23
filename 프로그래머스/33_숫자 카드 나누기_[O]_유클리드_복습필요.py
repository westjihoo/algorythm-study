# https://school.programmers.co.kr/learn/courses/30/lessons/135807

def solution(arrayA, arrayB):
    answer = 0

    gcdA = arrayA[0]
    gcdB = arrayB[0]

    for n in arrayA[1:] :
        gcdA = gcd(n, gcdA)

    for n in arrayB[1:] :
        gcdB = gcd(n, gcdB)

    divA = div(arrayA, gcdB)
    divB = div(arrayB, gcdA)

    if divA :
        answer = max(answer, gcdB)

    if divB :
        answer = max(answer, gcdA)

    return answer


def gcd(a, b) :
    while b > 0 :
        a, b = b, a % b
    return a

def div(arr, gcd) :
    for x in arr :
        if x % gcd == 0 :
            return 0
    return 1

arrayA = [14, 35, 119]
arrayB = [18, 30, 102]

arrayA = [10, 20]	
arrayB = [5, 17]


print(solution(arrayA, arrayB))