def f(x):
    return 2*x + 1
print(f(10))

def f(x):
    return x**2 + 2*x +1
print(f(10))



def mul(*valueS):
    
    output = 1
    for i in valueS:
        output *= i
    return output

print(mul(5,7,9,10))
        