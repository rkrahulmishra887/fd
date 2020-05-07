#MAR HIT
#Codevita 2019 Distribute books solution
#This code is encoded by Rahul Mishra(HIT)

N=int(input())
M = 1000000007
der=[0 for i in range(N+1)]
der[0]=1
der[1]=0
der[2]=1
for i in range(3,N+1):
    der[i]=((i-1)*(der[i-1]+der[i-2]))%M
print(der[N])
