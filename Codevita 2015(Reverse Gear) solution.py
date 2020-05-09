#MAR HIT
#Codevita solution Reverse Gear
#This code is encoded by Rahul Mishra(HIT)

def time(F,B,T,D):
    x=0
    count=0
    while(1):
        if(B<D):
            x=((F+B)*T)
            count+=x
            D=D-(B-F)
        else:
            x=(D*T)
            count+=x
            break
    return count


N=int(input())
for i in range(N):
    F,B,T,D=list(map(int, input().split()))
    print(time(F,B,T,D))




