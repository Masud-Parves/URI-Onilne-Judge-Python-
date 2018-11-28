list=[]

cntE=0
cntP=0
cntN=0

for i in range(0,5):
    list.append(int(input()))

for n in list:
    if(n%2)==0:
        cntE+=1
    if(n>0):
        cntP+=1
    if(n<0)
        cntN+=1

print("%d valor(es) par(es)" %cntE)
print("%d valor(es) impar(es)" %(5-cntE))
print("%d valor(es) positivo(s)" %cntP)
print("%d valor(es) negativo(s)" %cntN)
