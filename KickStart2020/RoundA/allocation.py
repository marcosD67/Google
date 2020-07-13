#Result: Accepted
#Easy Greedy solution. Just sort and traverse
for tc in range(int(input())):
    n, b = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    arr.sort()
    if b < arr[0]:
        print("Case #" + str(tc+1) + ": 0")
    else:
        count = 0
        for x in arr:
            if b-x >= 0:
                count+=1
            b -= x
        print("Case #" + str(tc+1) + ": " + str(count))