a=int(input())
s=0
t=a
while(t>0):
    b=t%10
    s=s+b**3
    t=t//10
if(a==s):
    print("yes")
else:
    print("no")
