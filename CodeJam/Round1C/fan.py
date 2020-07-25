#Result: 22/22 points
#Solved after the round ended. (During the competition I was off by one)

for tc in range(int(input())):
    print("Case #" + str(tc+1) + ":", end = ' ')
    x, y, m = input().split()
    
    x = int(x)
    y = int(y)
    startX, startY = 0, 0
    minTime = 0
    for i, el in enumerate(m):
        if el == 'E': x += 1
        elif el == 'W': x -= 1
        elif el == 'N': y +=1
        else: y -= 1
        if i+1 >= abs(x) + abs(y): 
            print(i+1)
            break
    else:print("IMPOSSIBLE")