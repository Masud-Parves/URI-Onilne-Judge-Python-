list=[]
cnt=0
for i in range(0,5):
    list.append(int(input()))

for n in list:
    if n%2==0:
        cnt+=1

print("%d valores pares" %cnt)
