#Result: Accepted
#This problem was more casework oriented
for tc in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    if n < 2:
        ans = 1
    else:
        ans = 0
        maxSoFar = -1
        for i in range(n):
            if i == 0: 
                if arr[i] > arr[i+1]: ans+=1
            elif i < n-1:
                if arr[i] > arr[i+1] and arr[i] > maxSoFar:
                    ans+=1
            else: #last element
                if arr[i] > maxSoFar: 
                    ans+=1
            maxSoFar = max(maxSoFar, arr[i])
    print("Case #" + str(tc+1) + ":", ans)