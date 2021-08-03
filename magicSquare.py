n = int(input("enter number : "))
arr = [[0 for j in range (n) ]for i in range (n)]
#step 1 
i1 = 0
j1 = n//2
k = 1

#step2
while k <= n ** 2:
    arr[i1][j1] = k
    if i1 == 0:
        i2 = i1 + n - 1
    else :
        i2 = i1 - 1
    if j1 == n - 1:
        j2 = j1 - n + 1
    else :
        j2 = j1 + 1 
    if arr[i2][j2] != 0:
        if i1 == n - 1:
            i2 = i1 - n + 1
        else :
            i2 = i1 + 1
        j2 = j1
    i1 = i2
    j1 = j2
    k = k + 1

for i in range (n):
    for j in range (n):
        print("%4d" %arr[i][j], end = '')
    print()
