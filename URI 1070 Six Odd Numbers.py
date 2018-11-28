num=int(input())
odd=0
cnt=0
if num%2==0:
    odd=num+1
    while(cnt!=6):
        print(odd)
        odd+=2
        cnt+=1
else:
    odd=num
    while(cnt!=6):
        print(odd)
        odd+=2
        cnt+=1
