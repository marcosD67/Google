#Result: 16/16
for tc in range(int(input())):
    ans = 0

    x, y, s = input().split()

    x, y = int(x), int(y)
    inc = 0
    if x < 0 or y < 0:
        inc = 1
    s = list(s)
    n = len(s)

    if n < 2:
        print("Case #{}:".format(tc+1), ans)
        continue
        
    start = -1
    for i in range(n):
        if s[i] != '?':
            start = i
            break

    if not inc:
        for i in range(start-1, -1, -1): #deal with ???????(C/J) cases
            s[i] = s[i+1]

        for i in range(start, n):
            if s[i] == '?':
                if not i:
                    if s[i+1] == 'C':
                        s[i] = s[i+1]
                    else:
                        s[i] = 'J'
                elif i < n-1:
                    if s[i+1] != '?':
                        if s[i+1] != s[i-1]: #check left and right sides: C?J or J?C
                            if s[i-1] == 'C': #C?J
                                s[i] = 'C'
                            else: s[i] = 'J' #J?C
                        else: #C?C or J?J
                            s[i] = s[i-1]
                    else: #next char is ?
                        s[i] = s[i-1] #keep CCCC... or JJJJ... going
                else:
                    s[i] = s[i-1] #last char should match the previous one

    #calculate final score
    for i in range(n-1):
        if s[i] != s[i+1]:
            if s[i] == 'C': ans += x #CJ
            else: ans += y #JC
    print("Case #{}:".format(tc+1), ans)