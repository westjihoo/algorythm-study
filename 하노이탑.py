def hanoi(n, start, end, sub):
    if n == 1 :
        print(start, "->", end)
    
    elif n >= 2 :
        hanoi(n-1, start, sub, end)
        print(start, "->", end)

        hanoi(n-1, sub, end, start)

n = int(input("원판의 개수 : "))
hanoi(n, "A", "B", "C")