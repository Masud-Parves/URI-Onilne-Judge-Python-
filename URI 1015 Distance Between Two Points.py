import math
X1, Y1=input().split(" ")
X2, Y2=input().split(" ")

Distance= math.sqrt((float(X2)-float(X1))**2+(float(Y2)-float(Y1))**2)
print("%.4f" %Distance)
