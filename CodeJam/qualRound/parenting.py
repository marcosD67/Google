#Result: 19/19 points

for tc in range(int(input())):
    arr = []
    for i in range(int(input())):
        l, r = [int(x) for x in input().split()]
        arr.append((l, r, i))
    imposs = False
    arr.sort(key = lambda x : x[0])
    cTask, jTask = tuple(), tuple()
    ans = [0] * len(arr)
    for i, (a, b, c) in enumerate(arr):
        if len(cTask) > 0:
            if a >= cTask[1]:
                cTask = (a, b, c)
                ans[c] = "C"
                continue
        else:
            cTask = (a, b, c)
            ans[c] = "C"
            continue
        if len(jTask) > 0:
            if a >= jTask[1]:
                jTask = (a, b, c)
                ans[c] = "J"
                continue
            else:
                imposs = True
                break
        else:
            ans[c] = "J"
            jTask = (a, b, c)
            continue
    if imposs:
        print("Case #" + str(tc+1) + ": IMPOSSIBLE")
    else:
        print("Case #" + str(tc+1) + ": ", *ans, sep = '')