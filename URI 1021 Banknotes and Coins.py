n=eval(input())
note100=note50=note20=note10=note5=note2=note1=0
money50=money25=money10=money5=money1=0

n=float("%.2f" %n)
if int(n/100) >= 1:
    note100=int(n/100)
    n-=(note100*100)

n=float("%.2f" %n)
if int(n/50) >= 1:
    note50=int(n/50)
    n-=(note50*50)

n=float("%.2f" %n)
if int(n/20) >= 1:
    note20=int(n/20)
    n-=(note20*20)

n=float("%.2f" %n)
if int(n/10) >= 1:
    note10=int(n/10)
    n-=(note10*10)

n=float("%.2f" %n)
if int(n/5) >= 1:
    note5=int(n/5)
    n-=(note5*5)

n=float("%.2f" %n)
if int(n/2) >= 1:
    note2=int(n/2)
    n-=(note2*2)

n=float("%.2f" %n)
if int(n/1) >= 1:
    note1=int(n/1)
    n-=(note1*1)

#poysa
n=float("%.2f" %n)
if int(n/0.50) >= 1:
    money50=int(n/0.50)
    n-=(money50*0.50)

n=float("%.2f" %n)
if int(n/0.25) >=1:
    money25=int(n/0.25)
    n-=(money25*0.25)

n=float("%.2f" %n)
if int(n/0.10) >= 1:
    money10=int(n/0.10)
    n-=(money10*0.10)

n=float("%.2f" %n)
if int(n/0.05) >= 1:
    money5=int(n/0.05)
    n-=(money5*0.05)

n=float("%.2f" %n)
if int(n/0.01) >= 1:
    money1=int(n/0.01)
    n-=(money1*0.01)

print("NOTAS:")
print("%d nota(s) de R$ 100.00\n%d nota(s) de R$ 50.00\n%d nota(s) de R$ 20.00\n%d nota(s) de R$ 10.00\n%d nota(s) de R$ 5.00\n%d nota(s) de R$ 2.00" %(note100,note50,note20,note10,note5,note2))
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00\n%d moeda(s) de R$ 0.50\n%d moeda(s) de R$ 0.25\n%d moeda(s) de R$ 0.10\n%d moeda(s) de R$ 0.05\n%d moeda(s) de R$ 0.01" %(note1,money50,money25,money10,money5,money1))
