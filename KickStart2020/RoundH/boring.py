#Result: Accepted: 7/19
#Naive solution. 4D Digit DP attempt got WA
for tc in range(int(input())):

    l, r = [int(x) for x in input().split()]
    ans = 0
    for i in range(l, r+1):
        isOdd = True
        valid = True
        s = str(i)
        for j in range(len(s)):
            if int(s[j]) % 2 != 0:
                if isOdd: isOdd = False
                else: 
                    valid = False
                    break
            else:
                if not isOdd: isOdd = True
                else: 
                    valid = False
                    break
        if valid: 
            ans += 1
    print("Case #" + str(tc+1) + ":", ans) 