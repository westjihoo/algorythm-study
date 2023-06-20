def merge(u, v):
    i = j = 0
    result = []
    while (i < len(u) and j < len(v)) :
        if u[i] < v[i] :
            result.append(u[i])
            i+=1
        else :
            result.append(v[j])
            j+=1
    
    result += u[i:]
    result += v[j:]

    return result


def mergesort(list) :
    n = len(list)
    if n <= 1 :
        return list
    else:
        mid = n // 2
        U = mergesort(list[:mid])
        V = mergesort(list[mid:])
        print(U,"|",V)
        return merge(U,V)


s = [25, 27, 10, 12, 37, 18, 20, 30, 35, 13, 14, 40, 47]
print("Before : ", s)
x = mergesort(s)
print("After : ", x)