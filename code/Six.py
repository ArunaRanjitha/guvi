w=int(input())
if((w%100!=0) and (w%4==0)) or (w%400==0):
    print("yes")
else:
    print("no")
