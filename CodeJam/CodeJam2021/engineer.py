#Result: 7/18
from itertools import permutations

for tc in range(int(input())):
    ans = []
    n, c = [int(x) for x in input().split()]
    hold = [i for i in range(1, n+1)]

    perms = list(permutations(range(1, n+1)))

    for arr in perms:
        score = 0
        temp = list(arr).copy()
        for i in range(1, n):
            ptr = temp.index(hold[i-1]) + 1 #index of ith smallest num

            score += abs(ptr-i) + 1 # R-L+1 (1-based)

            temp[(i-1):ptr] = temp[(i-1):ptr][::-1] #reverse arr[L:R]

        if score == c:
            ans = arr
            break
            
    if not ans:
        print("Case #{}:".format(tc+1), "IMPOSSIBLE")
    else:
        print("Case #{}:".format(tc+1), *ans)