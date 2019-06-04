def fib(fib1,fib2,count):
    count = count-1
    if(count==1):
        return fib2
    return fib(fib2,fib1+fib2,count)

print(fib(1,1,7))
    
	