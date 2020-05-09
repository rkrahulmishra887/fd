#MAR HIT
#Codvita Solution 2013(Zombie World)
#This code is encoded by Rahul Mishra


def solve(B,N,Z):
    for i in Z:
        if(B<i):
            print("NO")
            return False
        B-=(i//2 + i%2)
    print("YES")
    return True
try:
    
    B,N=list(map(int,input().split()))
    Z=list(map(int,input().split()))
except Exception:
    print("Invalid Input")
    exit(0)
solve(B,N,Z)





