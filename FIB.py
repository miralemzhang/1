m=int(input())
k=int(input())
def fib(n):
 assert n>=0
 if n<=1:
      return n
 else:
      return (fib(n-1) + k*fib(n-2))

print(fib(m), end=' ')
