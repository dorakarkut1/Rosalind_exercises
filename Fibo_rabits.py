
n = 32 #number of months
k = 2 # number of pairs reproduced each time

def Fibo(n,k):
    fibo = [1,1]
    for i in range(2,n+1):
        fibo.append(fibo[i-1]  + fibo[i-2]*k)
    print(fibo[n-1])

    return fibo[n-1]

Fibo(n,k)


