q=int(input())
rev=0
while(q>0):
    d=q%10
    rev=rev*10+d
    q=q//10
print(rev)
