code1 , unit1 , price1 = input().split(" ")
code2 , unit2 , price2 = input().split(" ")

total= float(int(unit1)*float(price1)+int(unit2)*float(price2))

print("VALOR A PAGAR: R$ %.2f" %total)
