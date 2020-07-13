#Result: Accepted
#This problem could be simplified into finding all strictly 
#increasing/decreasing subsequences with lengths greater than 4
for tc in range(int(input())):
    n = int(input())
    arr = [int(x) for x in input().split()]
    ans = 0
    if n > 4:
        decLength, incLength = 1, 1
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                incLength = 1
                decLength+=1
                if decLength > 4: 
                    ans+=1
                    decLength = 1
            elif arr[i] < arr[i-1]:
                decLength = 1
                incLength+=1
                if incLength > 4:
                    ans+=1
                    incLength = 1
    print("Case #" + str(tc+1) + ":", ans)