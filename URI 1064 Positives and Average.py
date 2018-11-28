list=[]
cnt=0
sum=0
for i in range(0,6):
    list.append(float(input()))

for n in list:
    if(n>0):
        cnt+=1
        sum+=n
sum=sum/cnt

print("%d valores positivos" %cnt)
print("%.1f" %sum)
