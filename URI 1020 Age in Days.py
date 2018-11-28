day=int(input())
year=int(day/365);
day=int(day%365);
month=int(day/30);
day=int(day%30);
print("%d ano(s)\n%d mes(es)\n%d dia(s)" %(year,month,day))
