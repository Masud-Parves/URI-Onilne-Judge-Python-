t=int(input())

list=[]

for i in range(0,t):

    list.append(int(input()))


for x in list:

    if x==0:

        print("NULL")

    elif x>0:

        if x%2==0:

            print("EVEN POSITIVE")

        else:

            print("ODD POSITIVE")

    else:

        if x%2==0:

            print("EVEN NEGATIVE")

        else:

            print("ODD NEGATIVE")
