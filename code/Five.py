p,q,r=input().split()
max(p,q,r)
if(p>q) and (p>r):
    print(p)
elif(q>p) and (q>r):
    print(q)
else:
    print(r)
