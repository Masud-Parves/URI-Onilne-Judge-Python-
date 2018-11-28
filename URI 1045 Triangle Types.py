A, B, C= input().split(" ")
A=float(A)
B=float(B)
C=float(C)

if A <B:
    temp = A;
    A = B;
    B = temp;

if B < C:
    temp = B;
    B = C;
    C = temp;
if A < B:
    temp = A;
    A = B;
    B = temp;

if A>=B+C:
    print("NAO FORMA TRIANGULO")
elif A*A==B*B+C*C:
    print("TRIANGULO RETANGULO")
elif A*A>B*B+C*C:
    print("TRIANGULO OBTUSANGULO")
elif A*A<B*B+C*C:
    print("TRIANGULO ACUTANGULO")
if A==B==C:
    print("TRIANGULO EQUILATERO")
elif (A==B and A!=C) or (A==C and B!=A) or (B==C and C!=A):
    print("TRIANGULO ISOSCELES")
