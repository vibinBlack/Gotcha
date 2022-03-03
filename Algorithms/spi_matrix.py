l=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for i in range(len(l)):
    for j in range(len(l[0])):
        print(l[i][j],end=" ")
    print("\n")
n=len(l)*len(l[0])
i=0
j=0
temp1=0
temp2=len(l)-1
while(n!=0):
    if i==temp1 and j<=temp2:
        ''
        print(l[i][j],end="")
        if n!=1:
            print("->",end="")
        if j==temp2:
            i=i+1
        else:
            j=j+1
    elif j==temp2 and i<=temp2:
        print(l[i][j],end="")
        if n!=1:
            print("->",end="")
        if i==temp2:
            j=j-1
        else:
            i=i+1
    elif i==temp2 and j<=temp2:
        print(l[i][j],end="")
        if n!=1:
            print("->",end="")
        if j==temp1:
            i=i-1
        else:
            j=j-1
    elif j==temp1 and i>=temp1:
        print(l[i][j],end="")
        if n!=1:
            print("->",end="")
        if i==temp1+1 and j==temp1:
            j=j+1
            temp1=temp1+1
            temp2=temp2-1
        elif j==temp1 and i>temp1:
            i=i-1
    n=n-1