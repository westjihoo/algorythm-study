# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    answer = ''

    # a ~ z
    # alphabet = [chr(x) for x in range(97, 123, 1)]
    # alphabet = [x for x in alphabet if not x in skip]
    alphabet = [chr(x) for x in range(97, 123, 1) if not chr(x) in skip]

    for c in s :
        idx = alphabet.index(c)
        idx += index
        while idx >= len(alphabet) :
            idx -= (len(alphabet))
        answer += alphabet[idx]
    return answer

s = "aukks"
skip = "wbqd"
index = 5

print(solution(s, skip, index))