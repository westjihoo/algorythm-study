def solution(X, Y):
    
    def divide(num):
        num = int(num)
        arr_num = []
        while num > 0 :
            arr_num.append(num%10)
            num = num//10
        return arr_num
    
    

    arr_X = divide(X)
    arr_Y = divide(Y)
    print(arr_X)
    print(arr_Y)

    answer = ''
    return answer


X="12321"
Y="42531"
r="321"

print(solution(X, Y))