row = int(input())
col = int(input())
mat = [[int(input()) for x in range(col)] for y in range(row)]
for i in range(row):
    for j in range(col-1,-1,-1):
        print(mat[j][i],end='')
    print()
