#Result: 10pts, TLE
#TLE for big test case. Binary Search would've been useful. 
for tc in range(int(input())):
    n, d = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    day = d
    visited = [False for i in range(n)]
    while True:
        while True:
            if day % arr[0] == 0:break
            day-=1
        visited[0] = True
        firstDay = day
        prevBus = 0
        notInOrder = False
        for i in range(day, d+1):
            if False in visited:
                for index, el in enumerate(arr):
                    if not visited[index]:
                        if i % el == 0:
                            if index-prevBus <= 1:
                                prevBus = index
                                visited[index] = True
            else:break
        if False not in visited: break
        else:
            day -= arr[0]
            visited = [False for i in range(n)]
    print("Case #" + str(tc+1) + ":", firstDay)