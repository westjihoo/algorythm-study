def draw_tower():
    print(tower1)
    print(tower2)
    print(tower3)
    print(cnt)
    print()

def hanoi(n, start, end, sub):
    
    global cnt, step
    print(cnt, step)

    if n == 1 :
        end.append(start.pop())
        cnt += 1
        draw_tower()

    elif n >= 2 :
        hanoi(n-1, start, sub, end)
        end.append(start.pop())
        cnt += 1
        draw_tower()
        hanoi(n-1, sub, end, start)

n = int(input("원판의 개수 : "))

step = 3
cnt = 0

tower1 = [3, 2, 1]
tower2 = []
tower3 = []

hanoi(n, tower1, tower3, tower2)

# scale = "          "
# drv = "     [DRV]"
#      [DRV]
# +--------+
# |COMPUTER|
# +--------+

# +--------+
# |        |
# |DISPLAY |
# |        |
# +--------+
# 
# 1========|2========|3========|