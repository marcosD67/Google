#Result: Accepted: 11/11
for tc in range(int(input())):

    n, k, s = [int(x) for x in input().split()]

    ans = (k-1)

    ans = min(ans + (n+1), ans + (k-s) + (n-s+1)) 
    print("Case #" + str(tc+1) + ": ", ans) 