sec=int(input())
h=int(sec/3600);
sec=int(sec%3600);
m=int(sec/60);
s=int(sec%60);
print("%d:%d:%d" %(h,m,s))
