A,B = input().split(" ");

A=int(A)
B=int(B)

C=B-A

if C<0:
    C=24+C
if A==B:
    print("O JOGO DUROU 24 HORA(S)")
else:
    print("O JOGO DUROU %d HORA(S)" %C)
