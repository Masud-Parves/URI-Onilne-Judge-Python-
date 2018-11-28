a=int(input())
b=int(input())

sum=0

for i in range(b+1,a):
    if i%2==1:
        sum+=i
print(sum)
