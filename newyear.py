r1,r2=map(int,input().split())
a,b=map(int,input().split())
r=max(r1,r2)
if 2*(r1+r2)<=a or 2*(r1+r2)<=b:
    print(r)
elif 2*r<=a and 2*r<=b:
    print(2*(r1+r2))
else:
    print(0)
