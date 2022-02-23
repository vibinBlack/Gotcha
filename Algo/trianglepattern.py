n = int(input("Enter triangle size:"))

print('Triangle')
for i in range(0,n):
    print(' '*(n-(i+1))+'*'*(i)+'*'+'*'*(i)+' '*(n-(i+1)))

print('Reverse Triangle')
for i in range(1,n):
    print(' '*i+'*'*(n-(i+1))+'*'+'*'*(n-(i+1))+' '*i)
