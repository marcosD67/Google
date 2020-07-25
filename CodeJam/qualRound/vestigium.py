#Result: 7/7 points

for tc in range(int(input())):
    n = int(input())
    matrix = [[] for i in range(n)]
    for i in range(n):
        matrix[i] = [int(x) for x in input().split()]
        trace = 0
        rowDups, colDups = 0, 0
    for index, el in enumerate(matrix):
        containsDups = False
        row = set()
        for i, x in enumerate(matrix[i]):
            if x in row: containsDups = True
            if index == i:trace+= matrix[i][i]
            row.add(x)  
        if containsDups:
            rowDups+=1
    for i in range(n):
        col = set()
        containsDups = False
        for j in range(n):
            if matrix[j][i] in col: containsDups = True
            col.add(matrix[j][i])
        if containsDups:colDups+=1
    print("Case #" + str(tc+1) + ": " + str(trace) + " " + \
    str(rowDups) + " " + str(colDups))