#Result: 7/7
for tc in range(int(input())):
    ans = 0

    n = int(input())

    arr = [int(x) for x in input().split()]
    hold = arr.copy()
    hold.sort()
    

    for i in range(1, n):
        ptr = arr.index(hold[i-1]) + 1 #index of ith smallest num

        ans += abs(ptr-i) + 1 # R-L+1 (1-based)


        arr[(i-1):ptr] = arr[(i-1):ptr][::-1] #reverse arr[L:R]

    print("Case #{}:".format(tc+1), ans)