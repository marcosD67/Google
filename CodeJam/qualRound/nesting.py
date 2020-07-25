#Result: 5/16 points
#This solution only works for cases with 1s and 0s
for tc in range(int(input())):
    s = input()
    if s.count('0') == len(s): # if only zeros
        print("Case #" + str(tc+1) + ": " + "0" * len(s))
    else:
        ptr1 = 0
        ans = ""
        count = 0
        while ptr1 <= len(s)-1:
            if s[ptr1] != '1':
                if count > 0:
                    ans += "("
                    ans += "1" * count
                    ans += ")"
                    count = 0
                ans += s[ptr1]
            else:count+=1
            ptr1 +=1
        if count > 0:
            ans += '('
            ans += "1" * count
            ans += ")"
        print("Case #" + str(tc+1) + ": ", *ans, sep='')