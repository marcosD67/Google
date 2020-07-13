#Result: Accepted
#Simple counting peaks of a vector problem
for tc in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    count = 0
    for i in range(1, n-1):
        if arr[i-1] < arr[i] and arr[i] > arr[i+1]:count+=1
    print("Case #" + str(tc+1) + ":", count)