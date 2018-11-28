list=[]

cnt=0

for i in range(0,6):
    list.append(float(input()))

for n in list:
    if(n>0):
        cnt+=1;

print("%d valores positivos" %cnt)
