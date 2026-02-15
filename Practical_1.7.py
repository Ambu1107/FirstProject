def fib(n,a=0,b=1):
    if n==0:
        return a
    else:
        return fib(n-1,b,a+b)
n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(fib(i),end=" ")