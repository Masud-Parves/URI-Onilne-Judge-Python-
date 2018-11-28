import math
A , B , C = input().split(" ")

A=float(A)
B=float(B)
C=float(C)

H=float(math.pow(B,2)-4*A*C)

if H>0 and A!=0:
    X1=((-B)+math.sqrt(math.pow(B,2)-(4*A*C)))/(2*A)
    X2=((-B)-math.sqrt(math.pow(B,2)-(4*A*C)))/(2*A)

    print("R1 = %.5f\nR2 = %.5f" %(X1, X2))
else:
    print("Impossivel calcular")
