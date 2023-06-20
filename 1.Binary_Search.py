
def location(list, low, high):
    print(x, low, high)
    if low>high:
        return 0
    else :
        mid = (low + high) // 2
        if x == list[mid] :
            return mid
        elif x > list[mid] :
            return location(list, mid+1, high)
        else :
            return location(list, low, mid-1)


s = [-1, 10, 12, 13, 14, 18, 20, 25, 27, 30, 35, 40, 45, 47]
x = 10
loc = location(s, 1, len(s)-1)
print("")
print('s = ', s)
print('x = ', x)
print('loc = ', loc)