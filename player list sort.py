def bs(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

a=["Ren","Alex","Ben","Zid","Chen"]
bs(a)
for i in range(len(a)):
    print(a[i],":",i+1,end=" ")
