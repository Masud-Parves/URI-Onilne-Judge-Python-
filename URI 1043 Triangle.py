A , B , C = input().split(" ")
A=float(A)
B=float(B)
C=float(C)

if A<B+C and B<A+C and C<C+A:
    print("Perimetro = %.1f" %(A + B + C))
else:
    print("Area = %.1f" %(C*(A + B)/2))
