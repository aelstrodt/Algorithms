memo_f = {0:1}
@time_decorator
def factorial(n):
    if n not in memo_f:
        memo_f[n] = n*factorial(n-1)
    return memo_f[n]
@time_decorator    
def i_factorial(n):
    if n ==1: return 1
    result = 1
    for i in range(2,n+1):
        result*=i
    return result

memo = {0:0,1:1}
@time_decorator
def fib(n):
    if not n in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
@time_decorator
def i_fib(n):
    if n == 0: return 1
    if n == 1: return 1
    last, current = 1, 1
    for i in range(2,n+1):
        current, last = current*i, current
    return current
times = []
def time_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        t1 = time.time()
        r = func(*args, **kwargs)
        t2 = time.time() - t1
        times.append(t2) 
        return r
    return wrapper
 