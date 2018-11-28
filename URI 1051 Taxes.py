A=float(input())

if A>=0 and A<=2000:
    print("Isento")
elif A>=2000.01 and A<=3000:
    A-=2000
    B=A*0.08
    print("R$ %.2f" %B)
elif A>=3000.01 and A<=4500:
    A-=3000
    B=A*0.18+80
    print("R$ %.2f" %B)
else:
    A-=4500
    B=A*0.28+350
    print("R$ %.2f" %B)
