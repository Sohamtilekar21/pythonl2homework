def bs(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]

a=[162,173,193,132,123,138,173,200,100]
c=len(a)
bs(a)
print("Range of the Heights is :",a[c-1]-a[0])
