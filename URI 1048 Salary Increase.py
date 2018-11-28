salary= float(input())
if 0<salary<=400 :
    result= salary+ (salary*15)/100
    persentage=15
    print("Novo salario: %.2lf" %result)
    print("Reajuste ganho: %.2lf" %(result-salary))
    print("Em percentual: "+ str(persentage) +" %" )
elif 400<salary<=800:
    result= salary+ (salary*12)/100
    persentage=12
    print("Novo salario: %.2lf" %result)
    print("Reajuste ganho: %.2lf" %(result-salary))
    print("Em percentual: "+ str(persentage) +" %" )
elif 800<salary<=1200:
    result= salary+ (salary*10)/100
    persentage=10
    print("Novo salario: %.2lf" %result)
    print("Reajuste ganho: %.2lf" %(result-salary))
    print("Em percentual: "+ str(persentage) +" %" )
elif 1200<salary<=2000: 
    result= salary+ (salary*7)/100
    persentage=7
    print("Novo salario: %.2lf" %result)
    print("Reajuste ganho: %.2lf" %(result-salary))
    print("Em percentual: "+ str(persentage) +" %" )
else:
    result= salary+ (salary*4)/100
    persentage=4
    print("Novo salario: %.2lf" %result)
    print("Reajuste ganho: %.2lf" %(result-salary))
    print("Em percentual: "+ str(persentage) +" %" )
