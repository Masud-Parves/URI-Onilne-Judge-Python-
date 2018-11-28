t=int(input())
cnt=0
cntO=0
list = []
for i in range(0,t):
    list.append(int(input()))

for x in list:
    if 10<=int(x)<=20:
        cnt+=1
    else:
        cntO+=1

print("%d in" %cnt)
print("%d out" %cntO)
