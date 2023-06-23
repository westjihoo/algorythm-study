# https://school.programmers.co.kr/learn/courses/30/lessons/135807

def solution(arrayA, arrayB):

    arrayA.sort()
    arrayB.sort()

    def find(sel_list, target_list):

        GDC = []
        for n in range(sel_list[0], 1, -1) :
            tmp_list = [ x%n for x in sel_list]
            tmp_list.sort()
            
            if tmp_list[-1] == 0:
                GDC.append(n)

        for gdc in GDC :
            tmp_list = [ x%gdc for x in target_list]
            tmp_list.sort()
            
            if not 0 in tmp_list :
                return gdc

        return 0
    
    return max(find(arrayA, arrayB), find(arrayB, arrayA))


arrayA = [14, 35, 119]
arrayB = [18, 30, 102]

arrayA = [10, 17]
arrayB = [5, 20]

print(solution(arrayA, arrayB))