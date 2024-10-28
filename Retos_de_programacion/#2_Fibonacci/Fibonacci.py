def Fibonacci(x,y,z):
        for _ in range(z):
            print(_,"->",x)
            x,y= y, x+y
            
Fibonacci(0,1,50)
