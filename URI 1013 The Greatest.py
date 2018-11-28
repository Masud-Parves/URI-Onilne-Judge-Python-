A, B, C= input().split(" ")
MaiorAB=int((int(A)+int(B)+int(abs(int(A)-int(B))))/2)
MaiorABC=int((int(MaiorAB)+int(C)+int(abs(int(MaiorAB)-int(C))))/2)
print("%d eh o maior" %MaiorABC)
