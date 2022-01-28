n=int(input())
a=list(input())
b=a.count(a[0])
c=[]
for i in a:
    if a.count(i)<b:
        b=a.count(i)
        c.append(i)
print(c[len(c)-1])